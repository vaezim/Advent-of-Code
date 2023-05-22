#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

template <typename T>
std::string VectorHash(const std::vector<T>& nums);

template <typename T>
void Distribute(std::vector<T>& nums);

template <typename T>
unsigned Balance(std::vector<T> nums, unsigned& loop_size=0);

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
    std::getline(file, line);

    /*
     * Part 1
     */
    std::vector<short> nums;
    std::istringstream iss(line);
    short n;
    while (iss >> n) {
        nums.push_back(n);
    }
    unsigned loop_size = 1;
    std::cout << "Answer of part 1: " << Balance(nums, loop_size) << '\n';

    /*
     * Part 2
     */
    std::cout << "Answer of part 2: " << loop_size << '\n';

    return 0;
}

template <typename T>
unsigned Balance(std::vector<T> nums, unsigned& loop_size) {
    std::unordered_map<std::string, unsigned> unique_hashes;
    std::string hash = VectorHash(nums);
    unsigned steps = 0;
    while (!unique_hashes.count(hash)) {
        unique_hashes.insert({hash, steps});
        Distribute(nums);
        hash = VectorHash(nums);
        steps++;
    }

    if (loop_size) {
        auto original = unique_hashes.find(hash);
        loop_size = steps - original->second;
    }

    return steps;
}

template <typename T>
void Distribute(std::vector<T>& nums) {
    size_t max_index = std::max_element(nums.begin(), nums.end()) - nums.begin();
    short value = nums[max_index];
    nums[max_index] = 0;
    size_t i = max_index+1;
    while (value) {
        if (i == nums.size()) i = 0;
        nums[i]++;
        value--;
        i++;
    }
}

template <typename T>
std::string VectorHash(const std::vector<T>& nums) {
    std::string res;
    for (const T& n: nums) {
        res.append(std::to_string(n));
        res.append(",");
    }
    return res;
}
