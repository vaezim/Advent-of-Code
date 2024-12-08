#include "utils.h"

Solver::Solver(const vector<string> &lines)
{
    vector<string> pageLines;
    vector<string> updateLines;
    bool inPage = true;
    for (const auto &line : lines) {
        if (line.size() < 3) {
            inPage = false;
            continue;
        }
        if (inPage) {
            pageLines.emplace_back(line);
        } else {
            updateLines.emplace_back(line);
        }
    }
    ParsePageNumbers(pageLines);
    ParseUpdates(updateLines);
}

int Solver::GetSumMidPageOfCorrectUpdates()
{
    int sum = 0;
    for (const auto &update : m_updates) {
        if (update.size() % 2 == 0) {
            std::cout << "Update size is even." << std::endl;
        }
        if (IsCorrectUpdate(update)) {
            sum += update[update.size()/2];
        }
    }
    return sum;
}

int Solver::GetSumMidPageOfIncorrectUpdates()
{
    int sum = 0;
    for (const auto &update : m_updates) {
        if (update.size() % 2 == 0) {
            std::cout << "Update size is even." << std::endl;
        }
        if (!IsCorrectUpdate(update)) {
            const auto &correctedUpdate = CorrectUpdate(update);
            sum += correctedUpdate[correctedUpdate.size()/2];
        }
    }
    return sum;
}

void Solver::FindCommonChild(unordered_set<int> &left, vector<int> &output)
{
    int child = -1;
    for (auto &n : left) {
        bool isCommonChild = true;
        for (auto &m : left) {
            if (n == m) continue;
            auto parent = m_nodes[m];
            if (!parent->IsChild(n)) {
                isCommonChild = false;
                break;
            }
        }
        if (isCommonChild) {
            child = n;
            break;
        }
    }
    if (child == -1) {
        std::cout << "Could not find common child of the remaining nodes." << endl;
        return;
    }
    output.push_back(child);
    left.erase(child);
}

vector<int> Solver::CorrectUpdate(const vector<int> &update)
{
    vector<int> output;
    unordered_set<int> left;
    for (auto &i : update) left.insert(i);
    while (output.size() < update.size()) {
        FindCommonChild(left, output);
    }
    return output;
}

bool Solver::IsCorrectUpdate(const vector<int> &update)
{
    for (int i{ (int)update.size()-1 }; i > 0; i--) {
        int n1 = update[i-1];
        int n2 = update[i];
        if (m_nodes.count(n1) == 0 || m_nodes.count(n2) == 0) {
            std::cout << "Node with value " << n1
                << " or " << n2 << " does not exist." << std::endl;
            return false;
        }
        auto node1 = m_nodes[n1];
        if (!node1->IsChild(n2)) {
            return false;
        }
    }
    return true;
}

bool Node::IsChild(int val) {
    for (const auto &child : m_children) {
        if (child->GetValue() == val) {
            return true;
        }
    }
    return false;
}

void Solver::ParseUpdates(const vector<string> &updateLines)
{
    m_updates.clear();
    for (const auto &line : updateLines) {
        string num;
        stringstream ss(line);
        m_updates.push_back({});
        while (getline(ss, num, ',')) {
            m_updates.back().push_back(stoi(num));
        }
    }
}

void Solver::ParsePageNumbers(const vector<string> &lines)
{
    for (const auto &line : lines) {
        if (line.size() < 2) { break; }
        int n1, n2;
        n1 = stoi(line.substr(0,2));
        n2 = stoi(line.substr(3,2));
        if (m_nodes.count(n1) == 0) {
            m_nodes[n1] = make_shared<Node>(n1);
        }
        if (m_nodes.count(n2) == 0) {
            m_nodes[n2] = make_shared<Node>(n2);
        }
        m_nodes[n1]->AddChild(m_nodes[n2]);
    }
}
