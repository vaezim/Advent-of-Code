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
    
    std::cout << "Answer of part 1: " << 0 << '\n';

    /*
     * Part 2
     */
    
    std::cout << "Answer of part 2: " << 0 << '\n';

    return 0;
}
