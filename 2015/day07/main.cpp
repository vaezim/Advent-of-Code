#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include "wire.h"


int main(int argc, char** argv) {

    /*
     * Reading File
     */
    if (argc != 3) {
        std::cout << "Usage: ./a.out [filename] [wireName]\n";
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
    Wire builder;
    builder.Build(lines);
    // builder.PrintCircuit();
    auto wire1 = Wire::GetWireByName(argv[2]);
    uint16_t emulatedVal1 = 0;
    if (wire1 != nullptr) {
        emulatedVal1 = wire1->Emulate();
    }
    std::cout << "Answer of part 1: " << emulatedVal1 << '\n';

    /*
     * Part 2
     */
    Wire builder2;
    builder2.Build(lines);
    auto wire2 = Wire::GetWireByName("b");
    wire2->OverrideOutput(emulatedVal1);
    auto wire3 = Wire::GetWireByName("a");
    std::cout << "Answer of part 2: " << wire3->Emulate() << '\n';

    return 0;
}
