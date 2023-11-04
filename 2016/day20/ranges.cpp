#include <algorithm>
#include "ranges.h"

void Ranges::Process()
{
    std::sort(m_vec.begin(), m_vec.end(),
        [](struct range& r1, struct range& r2) {return r1.start <= r2.start;});
    // Disp(m_vec);
    range curr = m_vec[0];
    for (const auto &r: m_vec) {
        // |--curr--|  |--r--|
        if (r.start > (curr.end + 1)) {
            m_nonOverlappingRanges.push_back(curr);
            curr = r;
        }
        // |--curr--/--r-- ...
        else {
            curr.end = std::max(curr.end, r.end);
        }
    }
    // Disp(m_nonOverlappingRanges);
}

int Ranges::GetLowestNonBlockedIP()
{
    if (m_nonOverlappingRanges.size() == 0) {
        return -1;
    }
    return m_nonOverlappingRanges[0].end + 1;
}

int Ranges::GetNumNonBlockedIP()
{
    int num = 0;
    for (auto i=0; i < m_nonOverlappingRanges.size()-1; i++) {
        range left = m_nonOverlappingRanges[i];
        range right = m_nonOverlappingRanges[i+1];
        num += (right.start - left.end - 1);
    }
    return num;
}

void Ranges::Disp(const std::vector<range> &vec) const
{
    for (const auto &item: vec) {
        std::cout << item.start << " - " << item.end << '\n';
    }
}