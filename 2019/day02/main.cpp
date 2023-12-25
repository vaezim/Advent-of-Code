#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>

#define TARGET_OP_CODE 19690720

int getOutputCode(std::vector<int>); // must be pass by value

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
    std::getline(file, line);
    std::istringstream iss(line);
    std::vector<int> nums;
    std::string n_str;

    /*
     * Part 1
     */
    while (std::getline(iss, n_str, ',')) {
        nums.push_back(std::atoi(n_str.c_str()));
    }
    // preprocessing
    nums[1] = 12; nums[2] = 2;
    std::cout << "Answer of part 1: " << getOutputCode(nums) << '\n';

    /*
     * Part 2
     */
    int target_noun, target_verb;
    for (int noun=0; noun < 100; noun++)
        for (int verb=0; verb < 100; verb++) {
            nums[1] = noun; nums[2] = verb;
            if (getOutputCode(nums) == TARGET_OP_CODE) {
                target_noun = noun;
                target_verb = verb;
                goto part2result;
            }
        }
    part2result:
    std::cout << "Answer of part 2: " << 100*target_noun+target_verb << '\n';

    return 0;
}

int getOutputCode(std::vector<int> nums) {
    for (size_t i=0; i < nums.size(); i+=4) {
        if (nums[i] == 99)
            break;
        else if (nums[i] == 1) {
            nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]; 
        } else if (nums[i] == 2) {
            nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]; 
        } else {
            std::cout << "Failed parsing nums!\n Exiting...\n";
            return -1;
        }
    }
    return nums[0];
}
