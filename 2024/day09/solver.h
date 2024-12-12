#include <vector>
#include <string>
#include <cstdint>


class Solver {
public:
    Solver(const std::string &line);
    ~Solver() = default;

    uint64_t SolvePart1();
    uint64_t SolvePart2();

private:
    std::vector<int> m_nums;
};