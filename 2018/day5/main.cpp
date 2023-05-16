#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

std::string React(std::string s, char c='0');  // provide the small letter e.g. a, b, c
std::string ReactChain(const std::string& s, char c='0');

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
    std::getline(file, line);

    /*
     * Part 1
     */
    std::cout << "Answer of part 1: " << ReactChain(line).length() << '\n';

    /*
     * Part 2
     */
    std::string alphabet = "abcdefghijklmnopqrstuvwxyz";
    std::vector<size_t> lens;
    for (const char& c: alphabet) { // count to 10 ;|
        lens.push_back(ReactChain(line, c).length());
    }
    std::cout << "Answer of part 2: " << *std::min_element(lens.begin(), lens.end()) << '\n';

    return 0;
}

std::string React(std::string s, char c) {
    if (!s.length()) {
        return "";
    }

    size_t i = 0;
    while (i < s.length()-1) {
        if (s[i] == '_') {
            i++;
            continue;
        }
        if (c != '0' && (s[i] == c || ((char)(s[i]+32)) == c)) {
            s[i] = '_';
        }
        else if (std::abs((int)s[i+1] - (int)s[i]) == 32) {
            s[i] = '_';
            s[i+1] = '_';
        }
        i++;
    }
    if (c != '0' && (s[i] == c || ((char)(s[i]+32)) == c)) { // last character
        s[i] = '_';
    }

    std::string res = "";
    for (const char& c: s) {
        if (c != '_') {
            res += c;
        }
    }

    return res;
}

std::string ReactChain(const std::string& s, char c) {
    std::string curr = s;
    while (true) {
        std::string next = React(curr, c);
        if (next.length() < curr.length()) {
            curr = next;
        } else {
            break;
        }
    }
    return curr;
}
