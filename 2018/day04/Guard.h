#pragma once
#include "Date.h"
#include <vector>
#include <utility>

class Guard {
public:
    Guard(const Date& date, int id);

    void AddSleep(unsigned, unsigned);
    unsigned GetTotalSleep() const;
    unsigned GetId() const { return m_id; }
    unsigned GetCommonMinute();
    unsigned GetCommonSleep() const { return m_commonSleep; }

private:
    Date m_date;
    int m_id;
    unsigned m_commonSleep;
    std::vector<std::pair<unsigned,unsigned>> m_sleepIntervals;

};
