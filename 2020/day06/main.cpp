#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>

#define toInt(X) static_cast<int>(X)

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
    lines.push_back(""); // final newline is not pushed.

    /*
     * Part 1
     */
    std::unordered_set<char> unique_letters;
    int sum = 0;
    for (std::string& line: lines) {
        if (line.length() == 0) {
            sum += unique_letters.size();
            unique_letters.clear();
        } else {
            for (char letter: line)
                unique_letters.insert(letter);
        }
    }
    std::cout << "Answer of Part 1: " << sum << '\n';

    /*
     * Part 2
     */
    sum = 0;
    int group_size = 0;
    std::vector<uint8_t> alpha_count(26);
    for (std::string& line: lines) {
        if (line.length() == 0) {
            for (size_t i=0; i < alpha_count.size(); i++) {
                sum += (alpha_count[i] == group_size);
                alpha_count[i] = 0;
            }
            group_size = 0;
        } else {
            group_size++;
            for (char& letter: line)
                alpha_count[toInt(letter) - toInt('a')]++;
        }
    }
    std::cout << "Answer of Part 2: " << sum << '\n';

    return 0;
}

