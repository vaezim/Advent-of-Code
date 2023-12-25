#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

bool is_valid(int, int, char, std::string);

int main(int argc, char** argv) {
    /*
     * Reading file
     */
    if (argc != 2) {
        std::cout << "Usage: ./a.out [filename]\n";
        return 0;
    }
    std::string FILENAME = argv[1];
    std::ifstream file; file.open(FILENAME);
    if (!file.is_open()) {
        std::cout << "Unable to open " << FILENAME << '\n';
        return 0;
    }

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line))
        lines.push_back(line);

    /*
     * Part 1
     */
    int min, max;
    char letter;
    size_t dash_idx, colon_idx;
    std::string passwd;
    unsigned valid_count = 0;
    for (const std::string& line: lines) {
        dash_idx = line.find('-'); colon_idx = line.find(':');
        min = std::stoi(line.substr(0,dash_idx));
        max = std::stoi(line.substr(dash_idx+1));
        letter = line[colon_idx-1];
        passwd = line.substr(colon_idx+2);
        
        valid_count += is_valid(min, max, letter, passwd);
    }
    std::cout << "Answer of part 1: " << valid_count 
              << '/' << lines.size() << '\n';

    /*
     * Part 2
     */
    valid_count = 0;
    for (const std::string& line: lines) {
        dash_idx = line.find('-'); colon_idx = line.find(':');
        min = std::stoi(line.substr(0,dash_idx));
        max = std::stoi(line.substr(dash_idx+1));
        letter = line[colon_idx-1];
        passwd = line.substr(colon_idx+2);
        
        if ((passwd[min-1] == letter) ^ (passwd[max-1] == letter))
            valid_count++;
    }
    std::cout << "Answer of part 2: " << valid_count 
              << '/' << lines.size() << '\n';

    return 0;
}

bool is_valid(int min, int max, char letter, std::string passwd) {
    size_t letter_count = std::count(passwd.begin(), passwd.end(), letter);
    return (min <= letter_count) && (letter_count <= max);
}
