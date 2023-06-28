#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include "program.h"


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
    std::string first_prog = lines[0].substr(0,lines[0].find(' '));

    /*
     * Part 1
     */
    for (const auto& spec: lines) {
        Program::ReadProgram(spec);
    }
    for (const auto& spec: lines) {
        Program::ReadChildren(spec);
    }
    auto prog = Program::GetProgram(first_prog);  // first program from the input
    auto root = prog->GetRoot();
    std::cout << "Answer of part 1: " << root->GetName() << '\n';

    /*
     * Part 2
     */
    Program::PopulateTowerWeights();
    uint16_t err = root->GetWeightError();
    std::cout << "Answer of part 2: " << err << '\n';

    return 0;
}
