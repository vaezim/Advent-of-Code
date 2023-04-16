#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define char2int(X) static_cast<int>(X)-static_cast<int>('0')

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
    std::string num;
    std::getline(file, num);

    /*
     * Part 1
     */
    int sum = 0;
    for (size_t i=0; i < num.length(); i++) {
        if (num[i % num.length()] == num[(i+1) % num.length()])
            sum += char2int(num[i]);
    }
    std::cout << "Answer of part 1: " << sum << '\n';

    /*
     * Part 2
     */
    sum = 0;
    for (size_t i=0; i < num.length(); i++) {
        if (num[i % num.length()] == num[(i+(int)num.length()/2) % num.length()])
            sum += char2int(num[i]);
    }
    std::cout << "Answer of part 2: " << sum << '\n';


    return 0;
}
