#include <map>
#include <list>
#include <string>


class Solver {
public:
    Solver(const std::string &nums);
    ~Solver() = default;

    size_t SolvePart1();
    size_t SolvePart2();

private:
    bool HasEvenNumberOfDigits(uint64_t n);
    std::pair<uint64_t, uint64_t> CutNumberInHalf(uint64_t val);

    size_t GetNumStonesAfterBlinkingForNTimes(uint64_t n, int N);

    std::list<uint64_t> m_list;
    std::map<std::pair<uint64_t, int>, size_t> m_map;
};