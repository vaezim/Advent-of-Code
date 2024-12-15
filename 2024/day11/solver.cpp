#include <sstream>
#include <iostream>
#include "solver.h"


Solver::Solver(const std::string &nums)
{
    std::stringstream ss(nums);
    uint64_t n;
    while (ss >> n) {
        m_list.emplace_back(n);
    }
}

size_t Solver::SolvePart1()
{
    size_t ans = 0;
    for (const auto &n : m_list) {
        ans += GetNumStonesAfterBlinkingForNTimes(n, 25);
    }
    return ans;
}

size_t Solver::SolvePart2()
{
    size_t ans = 0;
    for (const auto &n : m_list) {
        ans += GetNumStonesAfterBlinkingForNTimes(n, 75);
    }
    return ans;
}

size_t Solver::GetNumStonesAfterBlinkingForNTimes(uint64_t n, int N)
{
    if (N == 0) return 1;
    std::pair<uint64_t, int> key{ n, N };
    auto itr = m_map.find(key);
    if (itr != m_map.end()) { return itr->second; }
    // n == 0
    if (n == 0) {
        auto ans = GetNumStonesAfterBlinkingForNTimes(1, N-1);
        m_map[key] = ans;
        return ans;
    }
    // n has even number of digits
    if (HasEvenNumberOfDigits(n)) {
        auto halves = CutNumberInHalf(n);
        auto ans1 = GetNumStonesAfterBlinkingForNTimes(halves.first, N-1);
        auto ans2 = GetNumStonesAfterBlinkingForNTimes(halves.second, N-1);
        m_map[key] = ans1 + ans2;
        return ans1 + ans2;
    }
    // n *= 2024
    auto ans = GetNumStonesAfterBlinkingForNTimes(n * 2024, N-1);
    m_map[key] = ans;
    return ans;
}

bool Solver::HasEvenNumberOfDigits(uint64_t n)
{
    int length = 0;
    while (n > 0) {
        n /= 10;
        length++;
    }
    return (length % 2) == 0;
}

std::pair<uint64_t, uint64_t> Solver::CutNumberInHalf(uint64_t val)
{
    std::pair<uint64_t, uint64_t> halves;
    std::stringstream ss;
    ss << val;
    auto str = ss.str();
    halves.first = std::stoull(str.substr(0, str.size()/2));
    halves.second = std::stoull(str.substr(str.size()/2));
    return halves;
}