#include <bits/stdc++.h>

using namespace std;

class Node {
public:
    Node(int val) : m_value(val) {}
    ~Node() = default;

    bool IsChild(int val);
    int GetValue() { return m_value; }
    void AddChild(shared_ptr<Node> child) { m_children.push_back(child); }

private:
    int m_value{ 0 };
    vector<shared_ptr<Node>> m_children;
};

class Solver {
public:
    Solver(const vector<string> &lines);
    ~Solver() = default;

    int GetSumMidPageOfCorrectUpdates();
    int GetSumMidPageOfIncorrectUpdates();

private:
    vector<vector<int>> m_updates;
    unordered_map<int, shared_ptr<Node>> m_nodes;

    bool IsCorrectUpdate(const vector<int> &update);
    vector<int> CorrectUpdate(const vector<int> &update);
    void ParseUpdates(const vector<string> &updateLines);
    void ParsePageNumbers(const vector<string> &pageLines);
    void FindCommonChild(unordered_set<int> &left, vector<int> &output);
};