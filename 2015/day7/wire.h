#include <unordered_map>
#include <iostream>
#include <utility>
#include <memory>
#include <vector>
#include <string>


class Wire {
private:
enum class Gate{
    WIRE,
    AND,
    OR,
    NOT,
    RSHIFT,
    LSHIFT
};

public:
    explicit Wire(const std::string& name = "") : m_name(name){};
    using pWire = std::shared_ptr<Wire>;

    void SetVal(uint16_t val) { m_val = val; };
    void SetGate(const Gate& gate) { m_gate = gate; };
    void SetInput1(const std::string& input1) { m_inputs.first = input1; };
    void SetInput2(const std::string& input2) { m_inputs.second = input2; };

    void Build(const std::vector<std::string>& specs);
    uint16_t Emulate();
    void OverrideOutput(uint16_t val) { m_emulatedVal = val; };

    void PrintCircuit() const;
    static pWire GetWireByName(const std::string& name);

private:
    std::string m_name = "";
    uint16_t m_val = UINT16_MAX;
    uint16_t m_emulatedVal = UINT16_MAX;
    Gate m_gate = Gate::WIRE;
    std::pair<std::string, std::string> m_inputs;

    const std::unordered_map<std::string, Gate> m_gateMap {
        {"AND", Gate::AND}, {"OR", Gate::OR}, {"RSHIFT", Gate::RSHIFT}, {"LSHIFT", Gate::LSHIFT}
    };
};
