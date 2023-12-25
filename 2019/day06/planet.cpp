#include <memory>
#include <string>
#include <iostream>
#include <algorithm>
#include <unordered_set>

class Planet {
public:
    explicit Planet(const std::string& name) : 
        m_name(name){};
    
    void AddChild(const std::shared_ptr<Planet> child) {
        m_children.insert(child);
    }
    bool AddParent(const std::shared_ptr<Planet> parent) {
        if (!m_parent) {
            m_parent = parent;
            return true;
        }
        return false;
    }
    uint32_t GetDistanceToCOM() const {
        if (m_name == "COM") {
            return 0;
        }
        return 1 + m_parent->GetDistanceToCOM();
    }

    uint32_t GetDistanceToSAN(std::unordered_set<const Planet*>& visited) const {
        if (visited.count(this)) {
            return INT32_MAX;
        }
        if (m_name == "SAN") {
            return 0;
        }
        visited.insert(this);

        std::vector<uint32_t> branch_distances;
        if (m_parent) {
            branch_distances.push_back(1 + m_parent->GetDistanceToSAN(visited));
        }
        for (const auto& child: m_children) {
            branch_distances.push_back(1 + child->GetDistanceToSAN(visited));
        }

        return *std::min_element(branch_distances.begin(), branch_distances.end());
    }

private:
    std::string m_name = "";
    std::shared_ptr<Planet> m_parent = nullptr;
    std::unordered_set<std::shared_ptr<Planet>> m_children;
};
