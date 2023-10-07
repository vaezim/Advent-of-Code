#include <iostream>
#include <assert.h>
#include <fstream>
#include <list>

#define print(X) std::cout << X << '\n'

template <typename T>
void PrintList(const std::list<T>& list);

// assuming all items are unique
int Mix(const std::list<int>& nums);

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

    std::list<int> nums;
    int n;
    while (file >> n) {
        nums.push_back(n);
    }
    // PrintList(nums);

    /***** Part 1 *****/
    std::cout << "Answer of part 1: " << Mix(nums) << '\n';

    /***** Part 2 *****/
    std::list<int> l = {1, 2, 3, 4, 5, 6};
    auto it = l.begin();
    auto next = std::next(it,1);
    l.erase(it);
    l.insert(++next,1);
    // PrintList(l);
    std::cout << "Answer of part 2: " << 0 << '\n';

    return 0;
}

int Mix(const std::list<int>& _nums) {
    std::list<int> nums = _nums;
    int size = _nums.size();
    auto _it = _nums.begin();
    int _val;
    while (_it != _nums.end()) {
        // target item
        _val = *_it;
        if (_val % (size-1) == 0) {
            _it++;
            continue;
        }

        // find that item in nums
        auto it = nums.begin();
        while (*it != _val) {
            it++;
            if (it == nums.end())
                throw std::runtime_error("Target value not found!\n");
        }

        // find its target position
        auto next = std::next(it);
        if (next == nums.end())
            next = nums.begin();

        // erase it and insert it at position (next + _val)
        int steps = _val % (size-1);
        if (steps < 0) {
            steps = size-1 + steps;
        }
        for (size_t i=0; i < steps; i++) {
            next++;
            if (next == nums.end())
                next = nums.begin();
        }
        nums.erase(it);
        nums.insert(next, _val);

        // PrintList(nums);

        _it++;
    }
    assert(nums.size() == size);
    // PrintList(nums);

    // return nums[1000] + nums[2000] + nums[3000]
    auto zero_it = nums.begin();
    auto target_it = nums.begin();
    while (*zero_it != 0)
        zero_it++;
    int target_idxs[3] = {1000%size, 2000%size, 3000%size};
    int sum = 0;
    for (size_t i=0; i < 3; i++) {
        target_it = zero_it;
        int target_idx = target_idxs[i];
        for (size_t j=0; j < target_idx; j++) {
            target_it++;
            if (target_it == nums.end())
                target_it = nums.begin();
        }
        // print(*target_it);
        sum += *target_it;
    }

    return sum;
}

template <typename T>
void PrintList(const std::list<T>& list) {
    for (const T& item: list)
        std::cout << item << ", ";
    std::cout << '\n';
}
