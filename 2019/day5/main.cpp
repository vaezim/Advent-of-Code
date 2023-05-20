#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

void Diagnose(std::vector<int> nums, int input);
int ApplyOp(std::vector<int>& nums, size_t i, std::string op_str, int input);

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
    std::string num_str;
    std::vector<int> nums;
    while (std::getline(file, num_str, ',')) {
        nums.push_back(std::stoi(num_str));
    }

    /*
     * Part 1
     */
    std::cout << "Answer of part 1: ";
    Diagnose(nums, 1);

    /*
     * Part 2
     */
    std::cout << "Answer of part 2: ";
    Diagnose(nums, 5);

    return 0;
}

void Diagnose(std::vector<int> nums, int input) {
    unsigned i = 0;
    while (nums[i] != 99) {
        std::string op_str = std::to_string(nums[i]);
        int EIP = ApplyOp(nums, i, op_str, input);
        i = EIP;
    }
}

int ApplyOp(std::vector<int>& nums, size_t i, std::string op_str, int input) {
    // Op Code
    int op_code;
    if (op_str.length() == 1) {
        op_code = std::stoi(op_str);
    } else {
    op_code = std::stoi(op_str.substr(op_str.length()-2));
    }

    // Modes
    int mode[2] = {0, 0};
    int n[2];
    if (op_str.length() == 3) {
        mode[0] = std::stoi(op_str.substr(0,1));
    } else if (op_str.length() == 4) {
        mode[0] = std::stoi(op_str.substr(1,1));
        mode[1] = std::stoi(op_str.substr(0,1));
    }

    // 1st and 2nd Parameter
    if (mode[0] == 0) {
        n[0] = nums[nums[i+1]];
    } else {
        n[0] = nums[i+1];
    }
    if (mode[1] == 0) {
        n[1] = nums[nums[i+2]];
    } else {
        n[1] = nums[i+2];
    }

    // Operation
    switch (op_code) {
        case 1:
            nums[nums[i+3]] = n[0] + n[1];
            return i+4;
        case 2:
            nums[nums[i+3]] = n[0] * n[1];
            return i+4;
        case 3:
            if (mode[0] == 0) {
                nums[nums[i+1]] = input;
            } else {
                nums[i+1] = input;
            }
            return i+2;
        case 4:
            if (mode[0] == 0) {
                if (nums[nums[i+1]]) std::cout << nums[nums[i+1]] << '\n';
            } else {
                if (nums[i+1]) std::cout << nums[i+1] << '\n';
            }
            return i+2;
        case 5:
            if (n[0]) {
                return n[1];
            }
            return i+3;
        case 6:
            if (!n[0]) {
                return n[1];
            }
            return i+3;
        case 7:
            if (n[0] < n[1]) {
                nums[nums[i+3]] = 1;
            } else {
                nums[nums[i+3]] = 0;
            }
            return i+4;
        case 8:
            if (n[0] == n[1]) {
                nums[nums[i+3]] = 1;
            } else {
                nums[nums[i+3]] = 0;
            }
            return i+4;
        default:
            std::cout << "Wrong op code at position " << i << '\n';
            return -1;
    }
}
