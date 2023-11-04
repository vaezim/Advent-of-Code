#include <vector>
#include <iostream>

struct range {
    uint32_t start;
    uint32_t end;
};

class Ranges {
public:
    Ranges(const std::vector<range> &vec) : m_vec(vec) {
        Process();
    };
    ~Ranges() = default;

    int GetLowestNonBlockedIP();
    int GetNumNonBlockedIP();

private:
    void Process();
    void Disp(const std::vector<range> &vec) const;

    std::vector<range> m_vec;
    std::vector<range> m_nonOverlappingRanges;
};