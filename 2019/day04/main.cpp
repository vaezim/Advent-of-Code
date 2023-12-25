#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

bool IsValid1(const int& i);
bool IsValid2(const int& i);

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
    std::string line, r;
    file >> line;
    std::istringstream iss(line);
    int ranges[2], i=0;
    while (std::getline(iss, r, '-')) {
        ranges[i] = std::stoi(r);
        i++;
    }

    /*
     * Part 1
     */
    unsigned valids = 0;
    for (int i=ranges[0]; i <= ranges[1]; i++) {
        valids += IsValid1(i);
    }
    std::cout << "Answer of part 1: " << valids << '\n';

    /*
     * Part 2
     */
    valids = 0;
    for (int i=ranges[0]; i <= ranges[1]; i++) {
        valids += IsValid2(i);
    }
    std::cout << "Answer of part 2: " << valids << '\n';

    return 0;
}

bool IsValid1(const int& i) {
    std::string num = std::to_string(i);

    // rule 1
    bool found_double = false;
    for(size_t i=0; i < num.length()-1; i++) {
        if (num[i] == num[i+1]) {
            found_double = true;
            break;
        }
    }
    if (!found_double)
        return false;

    // rule 2
    for(size_t i=0; i < num.length()-1; i++) {
        if (num[i] > num[i+1])
            return false;
    }

    return true;
}

bool IsValid2(const int& i) {
    if (!IsValid1(i))
        return false;

    // rule 3
    std::string num = std::to_string(i);
    std::unordered_map<char, unsigned> char_map;
    for (const char& c: num) {
        if (char_map.count(c) == 0)
            char_map.insert({c, 0});
        char_map[c]++;
    }
    for (const auto& item: char_map) {
        if (item.second == 2)
            return true;
    }

    return false;
}
