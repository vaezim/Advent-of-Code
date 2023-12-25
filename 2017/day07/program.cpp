#include <sstream>
#include <iostream>
#include "program.h"

void Program::ReadProgram(const std::string& spec) {
    std::istringstream iss(spec);
    std::vector<std::string> tokens;
    std::string token;
    for (short i=0; i < 2; i++) {
        std::getline(iss, token, ' ');
        tokens.push_back(token);
    }

    std::string name = tokens[0];
    uint16_t weight = std::stoi(tokens[1].substr(1,tokens[1].size()-2));
    pProg prog = std::make_shared<Program>(name, weight);
    m_programMap.emplace(name, prog);
}

void Program::ReadChildren(const std::string& spec) {
    std::istringstream iss(spec);
    std::vector<std::string> tokens;
    std::string token;
    while (std::getline(iss, token, ' ')) {
        tokens.push_back(token);
    }

    std::string parent_name = tokens[0];
    pProg parent = GetProgram(parent_name);
    if (!parent) {
        std::cout << "Build children failed for program  [" << parent_name << "]\n";
        return;
    }
    if (tokens.size() <= 2) return;

    for (short i=3; i < tokens.size(); i++) {
        std::string child_name = tokens[i];
        if (i < tokens.size()-1) {
            child_name = child_name.substr(0, child_name.length()-1);
        }

        auto child = GetProgram(child_name);
        parent->AddChild(child);
        child->AddParent(parent);
    }
}

uint16_t Program::GetTowerWeight() {
    if (m_towerWeight != 0) return m_towerWeight;
    if (m_children.size() == 0) {
        m_towerWeight = m_weight;
        return m_towerWeight;
    }

    uint16_t sum_children = 0;
    for (pProg& child: m_children) {
        sum_children += child->GetTowerWeight();
    }
    m_towerWeight = m_weight + sum_children;
    return m_towerWeight;
}

void Program::PopulateTowerWeights() {
    for (const auto& item: m_programMap) {
        item.second->GetTowerWeight();
    }
}

uint16_t Program::GetWeightError() {
    // no child
    if (m_children.size() == 0) {
        return 0;
    }

    // find the anomaly child
    auto childrenTowerWeights = GetChildrenTowerWeights();
    auto idx = GetAnomalyIdx(childrenTowerWeights);
    if (idx == 255) return 0;

    // check the anomaly child
    pProg anomalyChild = m_children[idx];
    auto anomalyChildrenWeights = anomalyChild->GetChildrenTowerWeights();
    if (GetAnomalyIdx(anomalyChildrenWeights) == 255) {
        if (idx == 0)
            return anomalyChild->m_weight + childrenTowerWeights[1] - childrenTowerWeights[idx];
        return anomalyChild->m_weight + childrenTowerWeights[0] - childrenTowerWeights[idx];
    }

    return anomalyChild->GetWeightError();
}

std::vector<uint16_t> Program::GetChildrenTowerWeights() {
    std::vector<uint16_t> childrenTowerWeights;
    for (const auto& child: m_children) {
        childrenTowerWeights.push_back(child->GetTowerWeight());
    }
    return std::move(childrenTowerWeights);
}

pProg Program::GetProgram(const std::string& name) {
    auto progItem = m_programMap.find(name);
    if (progItem == m_programMap.end()) {
        std::cout << "Program [" << name << "] does not exist in the program map!\n";
        return nullptr;
    }
    return progItem->second;
}

pProg Program::GetRoot() {
    pProg parent = m_parent;
    if (!parent) {
        return GetProgram(m_name);
    }
    return m_parent->GetRoot();
}

size_t Program::GetAnomalyIdx(const std::vector<uint16_t>& nums) {
    if (nums.size() < 3 ) return 255;
    for (size_t i=0; i < nums.size()-2; i++) {
        if (nums[i] == nums[i+1] && nums[i] != nums[i+2]) return i+2;
        if (nums[i] == nums[i+2] && nums[i] != nums[i+1]) return i+1;
        if (nums[i+1] == nums[i+2] && nums[i+1] != nums[i]) return i;
    }
    return 255;
}
