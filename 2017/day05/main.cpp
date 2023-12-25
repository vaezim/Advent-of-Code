#include <algorithm>
#include <iostream>
#include <sstream>
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
    std::vector<int> nums(lines.size());
    unsigned i = 0;
    for (const std::string& line: lines) {
        nums[i] = std::stoi(line);
        i++;
    }

    unsigned curr_idx = 0, steps = 0;
    while (curr_idx < nums.size()) {
        nums[curr_idx]++;
        curr_idx += (nums[curr_idx] - 1);
        steps++;
    }
    std::cout << "Answer of part 1: " << steps << '\n';

    /*
     * Part 2
     */
    i = 0;
    for (const std::string& line: lines) {
        nums[i] = std::stoi(line);
        i++;
    }

    curr_idx = 0; steps = 0;
    while (curr_idx < nums.size()) {
        if (nums[curr_idx] >= 3) {
            nums[curr_idx]--;
            curr_idx += (nums[curr_idx] + 1);
        } else {
            nums[curr_idx]++;
            curr_idx += (nums[curr_idx] - 1);
        }
        steps++;
    }
    std::cout << "Answer of part 2: " << steps << '\n';

    return 0;
}
