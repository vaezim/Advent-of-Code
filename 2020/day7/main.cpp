#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>

#define PRINT(X) std::cout << X << '\n'

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
    std::unordered_map<std::string, u_int16_t> bag_map; // bag color --> num
    u_int16_t i = 0; // bag index
    std::string color;

    std::vector<std::string> tokens;
    std::string token;
    for (std::string& rule: lines) {
        std::stringstream ss(rule);
        while (std::getline(ss, token, ' '))
            tokens.push_back(token);
        
        // organizing the rule
        color = tokens[0]+tokens[1];
        bag_map[color] = i++;

        tokens.clear();
    }



    return 0;
}
