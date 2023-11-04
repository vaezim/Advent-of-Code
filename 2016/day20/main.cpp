#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include "ranges.h"


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
    std::vector<range> vec;
    for (const auto &line: lines) {
        std::istringstream iss(line);
        std::string left, right;
        std::getline(iss, left, '-');
        std::getline(iss, right);
        uint32_t start = static_cast<uint32_t>(std::stol(left));
        uint32_t end = static_cast<uint32_t>(std::stol(right));
        vec.push_back({start, end});
    }
    Ranges ranges(vec);
    auto result = ranges.GetLowestNonBlockedIP();
    std::cout << "[+] Answer of part 1: " << result << '\n';

    /*
     * Part 2
     */
    result = ranges.GetNumNonBlockedIP();
    std::cout << "[+] Answer of part 2: " << result << '\n';

    return 0;
}
