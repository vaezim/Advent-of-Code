#include "Guard.h"
#include <algorithm>

Guard::Guard(const Date& date, int id) {
    m_date = date;
    m_id = id;
}

void Guard::AddSleep(unsigned m1, unsigned m2) {
    std::pair<unsigned,unsigned> p(m1, m2);
    m_sleepIntervals.push_back(p);
}

unsigned Guard::GetTotalSleep() const {
    unsigned total = 0;
    for (const auto& p: m_sleepIntervals) {
        total += (p.second - p.first);
    }
    return total;
}

unsigned Guard::GetCommonMinute() {
    std::vector<unsigned> minutes(60);
    for (const auto& interval: m_sleepIntervals) {
        for (size_t i=interval.first; i < interval.second; i++) {
            minutes[i]++;
        }
    }
    m_commonSleep = *std::max_element(minutes.begin(), minutes.end());

    return (unsigned)std::distance(minutes.begin(),
                     std::max_element(minutes.begin(), minutes.end()));
}
