#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

short getDiffOfTwoStrings(const std::string&, const std::string&);

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
        std::cout << "Unable to open " << FILENAME << '\n';
        return 1;
    }
    std::string line;
    std::vector<std::string> lines;
    while (std::getline(file, line))
        lines.push_back(line);

    /*
     * Part 1
     */
    std::unordered_map<char, size_t> alpha_num;
    size_t exactly_two=0, exactly_three=0;
    for (const std::string& line: lines) {
        alpha_num.clear();
        for (const char& c: line) {
            if (alpha_num.count(c))
                alpha_num[c]++;
            else
                alpha_num[c] = 1;
        }
        for (const auto& item: alpha_num) {
            if (item.second == 2) {
                exactly_two++;
                break;
            }
        }
        for (const auto& item: alpha_num) {
            if (item.second == 3) {
                exactly_three++;
                break;
            }
        }
    }
    std::cout << "Answer of part 1: " << exactly_two*exactly_three << '\n';

    /*
     * Part 2
     */
    short diff_index, id1, id2;
    for (size_t i=0; i < lines.size(); i++) {
        for (size_t j=i+1; j < lines.size(); j++) {
            if ((diff_index = getDiffOfTwoStrings(lines[i], lines[j])) != -1) {
                id1 = i; id2 = j;
                goto part2result;
            }
        }
    }
    part2result:
    std::cout << "Answer of part 2: "
        << lines[id1].substr(0,diff_index)
        << lines[id1].substr(diff_index+1) << '\n';

    return 0;
}

short getDiffOfTwoStrings(const std::string& a, const std::string& b) {
    size_t diff_index = -1;
    for (size_t i=0; i < a.length(); i++) {
        if (a[i] == b[i])
            continue;
        if (diff_index == -1) {
            diff_index = i;
        } else {
            return -1;
        }
    }
    return diff_index;
}
