#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

bool IsValidPass(std::string pass, bool part=0);

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
    unsigned valid_passes = 0;
    for (const std::string& pass: lines) {
        valid_passes += IsValidPass(pass);
    }
    std::cout << "Answer of part 1: " << valid_passes << '\n';

    /*
     * Part 2
     */
    valid_passes = 0;
    for (std::string pass: lines) {
        valid_passes += IsValidPass(pass, 1);
    }
    std::cout << "Answer of part 2: " << valid_passes << '\n';

    return 0;
}

bool IsValidPass(std::string pass, bool part) {
    std::unordered_set<std::string> words;
    std::istringstream iss; iss.str(pass);
    std::string word;
    while (std::getline(iss, word, ' ')) {
        if (part)
            std::sort(word.begin(), word.end());
        if (words.count(word))
            return false;
        words.insert(word);
    }
    return true;
}

