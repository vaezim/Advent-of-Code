#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

bool SupportsTLS(const std::string& ip);
bool SupportsSSL(const std::string& ip);
bool IsABBA(const std::string& str);
bool HasABAPair(const std::string& str, const std::vector<std::string>& abaList);

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
    unsigned tlsNum = 0;
    for (const auto& line: lines) {
        tlsNum += SupportsTLS(line);
    }
    std::cout << "Answer of part 1: " << tlsNum << '\n';

    /*
     * Part 2
     */
    unsigned sslNum = 0;
    for (const auto& line: lines) {
        sslNum += SupportsSSL(line);
    }
    std::cout << "Answer of part 2: " << sslNum << '\n';

    return 0;
}

bool SupportsTLS(const std::string& ip) {
    bool insideBracket = false;
    bool foundABBA = false;
    std::string window;

    for (size_t i=0; i < ip.length()-3; i++) {
        window = ip.substr(i,4);

        // containing brackets
        if (window[0] == '[') {
            insideBracket = true;
            continue;
        }
        if (window[0] == ']') {
            insideBracket = false;
            continue;
        }
        if (window[1] == '[' || window[2] == '[' || window[3] == '[' ||
            window[1] == ']' || window[2] == ']' || window[3] == ']') {
                continue;
        }
        
        // check ABBA
        if (insideBracket && IsABBA(window)) {
            return false;
        }
        foundABBA = IsABBA(window) || foundABBA;
    }

    return foundABBA;
}

bool SupportsSSL(const std::string& ip) {
    std::vector<std::string> abaList;
    bool insideBracket = false;
    std::string window;

    // Outside of brackets
    for (size_t i=0; i < ip.length()-2; i++) {
        window = ip.substr(i,3);

        // containing brackets
        if (window[0] == '[') {
            insideBracket = true;
            continue;
        }
        if (window[0] == ']') {
            insideBracket = false;
            continue;
        }
        if (window[1] == '[' || window[2] == '[' ||
            window[1] == ']' || window[2] == ']') {
                continue;
        }
        
        // check ABA
        if (!insideBracket) {
            if (window[0] == window[2] && window[0] != window[1]) {
                abaList.push_back(window);
            }
        }
    }

    // Inside of brackets
    insideBracket = false;
    for (size_t i=0; i < ip.length()-2; i++) {
        window = ip.substr(i,3);

        // containing brackets
        if (window[0] == '[') {
            insideBracket = true;
            continue;
        }
        if (window[0] == ']') {
            insideBracket = false;
            continue;
        }
        if (window[1] == '[' || window[2] == '[' ||
            window[1] == ']' || window[2] == ']') {
                continue;
        }
        
        // check ABA
        if (insideBracket) {
            if (window[0] == window[2] && window[0] != window[1]) {
                if (HasABAPair(window, abaList)) {
                    return true;
                }
            }
        }
    }

    return false;
}

bool IsABBA(const std::string& str) {
    if (str.length() != 4) {
        std::cout << str <<  " has more than 4 characters!\n";
        return false;
    }
    
    return (str[0] == str[3]) && (str[1] == str[2]) && (str[0] != str[1]);
}

bool HasABAPair(const std::string& str, const std::vector<std::string>& abaList) {
    for (const auto& aba: abaList) {
        if (str[0] == aba[1] && str[1] == aba[0]) {
            return true;
        }
    }
    return false;
}
