#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>

#include "solver.h"


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
    Solver solver(line);
    size_t result = solver.SolvePart1();
    std::cout << "[+] Answer of part 1: " << result << '\n';

    /*
     * Part 2
     */
    result = solver.SolvePart2();
    std::cout << "[+] Answer of part 2: " << result << '\n';

    return 0;
}