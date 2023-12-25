#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

std::string FindMessage(const std::vector<std::string>& words, unsigned part=1);

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
    std::string msg = FindMessage(lines);
    std::cout << "Answer of part 1: " << msg << '\n';

    /*
     * Part 2
     */
    msg = FindMessage(lines, 2);
    std::cout << "Answer of part 2: " << msg << '\n';

    return 0;
}

std::string FindMessage(const std::vector<std::string>& words, unsigned part) {
    std::string msg = "";
    std::vector<unsigned> char_nums(26, 0);
    unsigned length = words[0].length();
    for (short i=0; i < length; i++) {
        for (short j=0; j < char_nums.size(); j++) char_nums[j] = 0;
        for (const std::string& words: words) {
            char_nums[words[i] - 'a'] += 1;
        }
        unsigned max_char;
        if (part == 1) {
            max_char = std::max_element(char_nums.begin(),char_nums.end()) - char_nums.begin();
        } else {
            max_char = std::min_element(char_nums.begin(),char_nums.end()) - char_nums.begin();
        }
        msg += (char)(max_char + 'a');
    }
    return msg;
}
