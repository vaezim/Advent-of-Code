#include <iostream>
#include <fstream>
#include <unordered_set>
#include <string>
#include <vector>


int main(int argc, char** argv) {
    if (argc != 2) {
        std::cout << "Usage: ./a.out [filename]\n";
        return 0;
    }

    /*
     * preprocessing
     */
    std::string FILENAME = argv[1];
    std::ifstream file;

    file.open(FILENAME);
    if (!file.is_open()) {
        std::cout << "Unable to open file " << FILENAME << '\n';
        return 0;
    }

    short num, target=2020;
    std::vector<short> nums;
    std::unordered_set<short> visited;
    std::string line;

    while (std::getline(file, line)) {
        num = std::stoi(line);
        nums.push_back(num);
        visited.insert(num);
    }
    file.close();

    /*
     * Part 1
     */
    for (short num: nums) {
        // if [target-num] exists, print the result.
        if (visited.count(target-num)) {
            std::cout << "Answer of Part 1: " 
                      << num*(target-num) << '\n';
            break;
        }
    }

    /*
     * Part 2
     */
    for (size_t i=0; i < nums.size(); i++)
        for (size_t j=i+1; j < nums.size(); j++)
            if (visited.count(target-nums[i]-nums[j])) {
                std::cout << "Answer of Part 2: " 
                      << nums[i]*nums[j]*(target-nums[i]-nums[j]) << '\n';
                return 0;
            }

    return 0;
}
