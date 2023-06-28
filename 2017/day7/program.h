#include <string>
#include <vector>
#include <memory>
#include <unordered_map>

class Program;
using pProg = std::shared_ptr<Program>;

class Program {
public:
    Program(const std::string& name="", const uint16_t& weight=0) : 
        m_name(name), m_weight(weight) {};

    static void ReadProgram(const std::string& spec);
    static void ReadChildren(const std::string& spec);
    static pProg GetProgram(const std::string& name);
    static void PopulateTowerWeights();

    uint16_t GetWeightError();  // run on root and after running PopulateTowerWeights()
    pProg GetRoot();

    void AddParent(const pProg parent) { m_parent = parent; };
    void AddChild(const pProg child) { m_children.push_back(child); };
    std::string GetName() { return m_name; };
    uint16_t GetWeight() { return m_weight; };

private:
    std::string m_name;
    uint16_t m_weight;
    uint16_t m_towerWeight = 0;
    pProg m_parent = nullptr;
    std::vector<pProg> m_children;

    uint16_t GetTowerWeight();
    size_t GetAnomalyIdx(const std::vector<uint16_t>& nums);
    std::vector<uint16_t> GetChildrenTowerWeights();
};

static std::unordered_map<std::string, pProg> m_programMap;
