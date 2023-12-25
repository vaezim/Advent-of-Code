#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <string>
#include <vector>
#include "Date.h"
#include "Guard.h"

#define print(X) std::cout << X << '\n';
void PrintVector(const std::vector<Date>& dates);

int main(int argc, char** argv) {

    /*
     * Reading File
     */
    if (argc != 2) {
        std::cout << "Usage: ./a.out [filename]\n";
        return 1;
    }
    std::string FILENAME = argv[1];
    std::ifstream file; file.open(FILENAME);
    if (!file.is_open()) {
        throw std::runtime_error("Unable to open file " + FILENAME);
    }
    std::string line;
    std::vector<std::string> lines;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    /*
     * Part 1
     */
    std::vector<Date> dates;
    for (const std::string& line: lines) {
        Date d(line.substr(1,16), line.substr(19));
        dates.push_back(d);
    }
    std::sort(dates.begin(), dates.end());
    // PrintVector(dates);

    std::unordered_map<int, std::shared_ptr<Guard>> guards;  // id --> p_guard
    for (const Date& date: dates) {
        unsigned sleep, wake;
        int id = date.GetGuardId(), last_added_id;
        if (id >= 0) {  // a guard began shift
            if (guards.count(id) == 0) {
                Guard guard(date, id);
                std::shared_ptr<Guard> p_guard = std::make_shared<Guard>(guard);
                guards.insert({id, p_guard});
            }
            last_added_id = id;
        } else if (date.GetEvent()[0] == 'f') {  // falls sleep
            sleep = date.GetMinute();
            
        } else if (date.GetEvent()[0] == 'w') {  // wakes up
            wake = date.GetMinute();
            guards[last_added_id]->AddSleep(sleep,wake);
        }
    }
    
    int max_id, max_sleep = 0;
    for (const auto& item: guards) {
        int total_sleep = item.second->GetTotalSleep();
        if (total_sleep > max_sleep) {
            max_sleep = total_sleep;
            max_id = item.first;
        }
    }
    unsigned most_common_minute = guards[max_id]->GetCommonMinute();
    std::cout << "Answer of part 1: " << (max_id * most_common_minute) << '\n';

    /*
     * Part 2
     */
    max_id = 0;
    max_sleep = 0;
    unsigned common_minute;
    for (const auto& item: guards) {
        unsigned c_minute = item.second->GetCommonMinute();
        unsigned c_sleep = item.second->GetCommonSleep();
        if (c_sleep > max_sleep) {
            max_id = item.first;
            max_sleep = c_sleep;
            common_minute = c_minute;
        }
    }
    std::cout << "Answer of part 2: " << max_id * common_minute << '\n';

    return 0;
}

void PrintVector(const std::vector<Date>& dates) {
    for (const Date& d: dates) {
        d.Print();
    }
}
