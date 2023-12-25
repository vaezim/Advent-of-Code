#include <iostream>
#include <sstream>
#include "Date.h"

Date::Date(const std::string& date_str,
           const std::string& event) {
    m_dateStr = date_str; // 1518-08-05 00:39
    m_event = event;
    Build();
}

void Date::Build() {
    m_year = std::stoi(m_dateStr.substr(0,4));
    m_month = std::stoi(m_dateStr.substr(5,2));
    m_day = std::stoi(m_dateStr.substr(8,2));
    m_hour = std::stoi(m_dateStr.substr(11,2));
    m_minute = std::stoi(m_dateStr.substr(14,2));
}

int Date::GetGuardId() const {
    if (m_event[0] != 'G') {
        return -1;
    }
    std::istringstream iss(m_event);
    std::string id;
    while (std::getline(iss, id, ' ')) {
        if (id[0] == '#') {
            return std::stoi(id.substr(1));
        }
    }
    return -2;
}

void Date::Print() const {
    std::cout << m_year << '/' << m_month << '/' << m_day << "@";
    if (m_hour != 0) {
        std::cout << m_hour;
    } else {
        std::cout << "00";
    }
    std::cout << ":" << m_minute << "--> " << m_event << '\n';
}

bool Date::operator<(const Date& d) const {
    if (this->m_year > d.m_year) return false;
    if (this->m_year < d.m_year) return true;
    if (this->m_month > d.m_month) return false;
    if (this->m_month < d.m_month) return true;
    if (this->m_day > d.m_day) return false;
    if (this->m_day < d.m_day) return true;
    if (this->m_hour > d.m_hour) return false;
    if (this->m_hour < d.m_hour) return true;
    if (this->m_minute > d.m_minute) return false;
    if (this->m_minute < d.m_minute) return true;
    return false;
}

bool Date::operator==(const Date& d) const {
    return (this->m_year == d.m_year) &&
           (this->m_month == d.m_month) &&
           (this->m_day == d.m_day) &&
           (this->m_hour == d.m_hour) &&
           (this->m_minute == d.m_minute);
}

bool Date::operator>(const Date& d) const {
    return !(*this < d || *this == d);
}
