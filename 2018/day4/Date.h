#pragma once
#include <string>

class Date {
public:
    explicit Date(const std::string& date_str,
                  const std::string& event);
    Date() = default;

    int GetGuardId() const;
    const std::string& GetEvent() const { return m_event; }
    unsigned GetMinute() const { return m_minute; }

    bool operator<(const Date& d) const;
    bool operator>(const Date& d) const;
    bool operator==(const Date& d) const;

    void Print() const;

private:
    void Build();

    std::string m_dateStr;
    std::string m_event;
    unsigned m_year, m_month, m_day, m_hour, m_minute;
};
