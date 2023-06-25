#include <sstream>
#include "ctype.h"
#include "wire.h"

// Global circuit variable
std::unordered_map<std::string, Wire::pWire> m_circuit;

void Wire::Build(const std::vector<std::string>& specs) {
    // Clear previously built circuit
    m_circuit.clear();

    for (const std::string& spec: specs) {
        
        // Tokenize
        std::vector<std::string> tokens;
        std::string token;
        std::istringstream iss(spec);
        while (std::getline(iss, token, ' ')) {
            tokens.push_back(token);
        }

        // Create the wire using name constructor
        std::string name = tokens.back();
        pWire wire;
        auto wire_item = m_circuit.find(name);
        if (wire_item != m_circuit.end()) {
            wire = wire_item->second;
        } else {
            wire = std::make_shared<Wire>(name);
            m_circuit[name] = wire;
        }

        // A -> C
        // num -> C
        if (tokens.size() == 3) {
            std::string A = tokens[0];
            if (isdigit(A[0])) {
                uint16_t val = std::stoi(A);
                wire->SetVal(val);
            } else {
                wire->SetInput1(A);
            }
        }

        // NOT A -> C
        else if (tokens.size() == 4) {
            wire->SetGate(Gate::NOT);
            std::string A = tokens[1];
            if (isdigit(A[0])) {
                uint16_t val = std::stoi(A);
                wire->SetVal(val);
            } else {
                wire->SetInput1(A);
            }
        }

        // A [Gate] B -> C
        // A [SHIFT] num -> C
        else if (tokens.size() == 5) {
            Gate gate = m_gateMap.find(tokens[1])->second;
            wire->SetGate(gate);
            std::string A = tokens[0];
            if (isdigit(A[0])) {  // A
                uint16_t val = std::stoi(A);
                wire->SetVal(val);
            } else {
                wire->SetInput1(A);
            }
            std::string B = tokens[2];
            if (isdigit(B[0])) {  // B
                uint16_t val = std::stoi(B);
                wire->SetVal(val);
            } else {
                wire->SetInput2(B);
            }
        } else {
            std::cout << "Wrong Spec: " << spec << '\n';
        }
    }

    std::cout << "\033[1;32m[*] Circuit successfully built.\033[0m\n";
}

uint16_t Wire::Emulate() {

    // check m_emulatedVal
    if (m_emulatedVal != UINT16_MAX) {
        return m_emulatedVal;
    }

    // both ports are empty, then return m_val
    if (m_inputs.first.length() == 0 && m_inputs.second.length() == 0) {
        m_emulatedVal = m_val;
        return m_emulatedVal;
    }

    // m_gate is NOT
    if (m_gate == Gate::NOT) {
        std::string input1Name = m_inputs.first;
        auto input1Wire = GetWireByName(input1Name);
        uint16_t input1Val = input1Wire->Emulate();
        m_emulatedVal = (uint16_t)~input1Val;
        return m_emulatedVal;
    }

    // one input is non-empty and m_val == UINT16_MAX
    if (m_inputs.first.length() != 0 && m_inputs.second.length() == 0 && m_val == UINT16_MAX) {
        std::string input1Name = m_inputs.first;
        auto input1Wire = GetWireByName(input1Name);
        m_emulatedVal = input1Wire->Emulate();
        return m_emulatedVal;
    }

    // either of inputs are non-empty and m_val != UINT16_MAX
    if (m_inputs.first.length() != 0 || m_inputs.second.length() != 0) {
        std::string input1Name = m_inputs.first;
        auto input1Wire = GetWireByName(input1Name);
        uint16_t input1Val = input1Wire != nullptr ? input1Wire->Emulate() : m_val;

        std::string input2Name = m_inputs.second;
        auto input2Wire = GetWireByName(input2Name);
        uint16_t input2Val = input2Wire != nullptr ? input2Wire->Emulate() : m_val;

        switch (m_gate) {
            case Gate::AND:
                m_emulatedVal = (uint16_t)(input1Val & input2Val); return m_emulatedVal;
            case Gate::OR:
                m_emulatedVal = (uint16_t)(input1Val | input2Val); return m_emulatedVal;
            case Gate::RSHIFT:
                m_emulatedVal = (uint16_t)(input1Val >> input2Val); return m_emulatedVal;
            case Gate::LSHIFT:
                m_emulatedVal = (uint16_t)(input1Val << input2Val); return m_emulatedVal;
            default:
                std::cout << "Unknown gate enum: " << (int)m_gate << " in wire " << m_name << '\n';
                return m_emulatedVal;
        }
    }

    std::cout << "Unknown wire setup.\n";
    return UINT16_MAX;
}

void Wire::PrintCircuit() const {
    for (const auto& item: m_circuit) {
        std::cout << "Wire " << item.first << " :\n";
        auto wire = item.second;
        std::cout << "\t Inputs: " << wire->m_inputs.first << ", " << wire->m_inputs.second << '\n';
        std::cout << "\t Gate: " << (int)wire->m_gate << '\n';
        std::cout << "\t Val: " << wire->m_val << '\n';
    }
}

Wire::pWire Wire::GetWireByName(const std::string& name) {
    if (name.length() == 0) {
        return nullptr;
    }
    auto wire = m_circuit.find(name);
    if (wire == m_circuit.end()) {
        std::cout << "Wire " << name << " could not be found!\n";
        return nullptr;
    }
    return wire->second;
}
