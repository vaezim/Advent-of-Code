#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

int getFuel1(int);
long int getFuel2(int);

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
    int num;
    long long sum = 0;
    for (const std::string& line: lines) {
        num = std::stoi(line);
        sum += getFuel1(num);
    }
    std::cout << "Answer of part 1: " << sum << '\n';

    /*
     * Part 2
     */
    sum = 0;
    for (const std::string& line: lines) {
        num = std::stoi(line);
        sum += getFuel2(num);
    }
    std::cout << "Answer of part 2: " << sum << '\n';

    return 0;
}

int getFuel1(int num) {
    return std::max(static_cast<int>(std::floor(num/3)) - 2, 0);
}

long int getFuel2(int num) {
    long int sum = 0;
    int fuel = getFuel1(num);
    while (fuel) {
        sum += fuel;
        fuel = getFuel1(fuel);
    }
    return sum;
}
