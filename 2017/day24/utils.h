#include <vector>
#include <string>
#include <unordered_set>

struct Pin {
    uint16_t side1{};
    uint16_t side2{};

    bool operator == (const Pin &other) const {
        return side1 == other.side1 && side2 == other.side2;
    }
};
struct PinHash {
    uint32_t operator () (const Pin &pin) const {
        return static_cast<uint32_t>(pin.side1 << 16) + 
               static_cast<uint32_t>(pin.side2);
    }
};
using PinSet = std::unordered_set<Pin, PinHash>;

class Pins {
public:
    Pins(const std::vector<std::string> &lines);
    ~Pins() = default;

    /* Strength of the strongest bridge */
    uint32_t GetStrongestBridge() const;
    /* Strength of the longest bridge */
    uint32_t GetLongestBridge() const;

private:
    void ParseLines();
    void GetStrongestBridge(const uint16_t &lastPinSide, PinSet &pins, uint32_t sum) const;
    void GetLongestBridge(const uint16_t &lastPinSide, PinSet &pins, uint32_t sum) const;

    PinSet m_pins;
    mutable uint32_t m_maxSum{ 0 };
    mutable uint32_t m_longest{ 0 };
    const std::vector<std::string> &m_lines;
};