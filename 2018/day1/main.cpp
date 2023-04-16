#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>


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
    int freq = 0, drift;
    for (const std::string& line: lines) {
        drift = std::stoi(line.substr(1));
        if (line[0] == '+')
            freq += drift;
        else if (line[0] == '-')
            freq -= drift;
        else {
            std::cout << "Invalid sing!" << '\n';
            return 1;
        }
            
    }
    std::cout << "Answer of part 1: " << freq << '\n';

    /*
     * Part 2
     */
    freq = 0;
    std::unordered_set<int> freqs = {0};
    bool duplicate_found = false;
    while (true) {
        // iterate through drifts
        for (const std::string& line: lines) {
            drift = std::stoi(line.substr(1));
            if (line[0] == '+')
                freq += drift;
            else if (line[0] == '-')
                freq -= drift;
            else {
                std::cout << "Invalid sing!" << '\n';
                return 1;
            }

            // if a freq was seen before
            if (freqs.count(freq)) {
                duplicate_found = true;
                break;
            }
            freqs.insert(freq);
        }
        // one iteration completed. did we find a duplicate?
        if (duplicate_found)
            break;
    }
    std::cout << "Answer of part 2: " << freq << '\n';


    return 0;
}
