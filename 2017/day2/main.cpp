#include <algorithm>
#include <limits.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>

int getDiffOfTwoDivisibles(const std::vector<int>&);

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
    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    /*
     * Part 1
     */
    std::istringstream iss;
    int min, max, num, result=0;
    for (const std::string& line : lines) {
        iss.str(line); iss.clear();
        min = INT_MAX; max = INT_MIN;
        while (iss >> num) {
            min = std::min(num, min);
            max = std::max(num, max);
        }
        result += (max - min);
    }
    std::cout << "Answer of part 1: " << result << '\n';

    /*
     * Part 2
     */
    result=0;
    std::vector<int> nums;
    for (const std::string& line : lines) {
        iss.str(line); iss.clear();
        while (iss >> num) {
            nums.push_back(num);
        }
        result += getDiffOfTwoDivisibles(nums);
        nums.clear();
    }
    std::cout << "Answer of part 2: " << result << '\n';

    return 0;
}

int getDiffOfTwoDivisibles(const std::vector<int>& nums) {
    for (const int& x : nums) {
        for (const int& y : nums) {
            if ((x!=y) && ((x%y==0) || (y%x==0))) {
                return (int)(std::max(x,y)/std::min(x,y));
            }
        }
    }
    return -1;
}
