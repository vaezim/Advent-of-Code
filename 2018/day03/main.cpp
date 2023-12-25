#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>


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
    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    /*
     * Part 1
     */
    size_t grid[1000][1000] = {};
    int id, x, y, w, h;
    const std::regex r("#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)");
    std::smatch sm;
    for (const std::string& line: lines) {
        if (std::regex_search(line, sm, r)) {
            id = std::stoi(sm[1]);
            x = std::stoi(sm[2]);
            y = std::stoi(sm[3]);
            w = std::stoi(sm[4]);
            h = std::stoi(sm[5]);
        }
        for (size_t i=x; i < x+w; i++)
            for (size_t j=y; j < y+h; j++) {
                grid[i][j]++;
            }
    }
    size_t count = 0;
    for (size_t i=0; i < 1000; i++)
        for (size_t j=0; j < 1000; j++)
            count += (grid[i][j] >= 2);
    std::cout << "Answer of part 1: " << count << '\n';

    /*
     * Part 2
     */
    size_t intact_id = 0;
    bool remained_intact = true;            
    find_intact:
    for (const std::string& line: lines) {
        remained_intact = true;
        if (std::regex_search(line, sm, r)) {
            id = std::stoi(sm[1]);
            x = std::stoi(sm[2]);
            y = std::stoi(sm[3]);
            w = std::stoi(sm[4]);
            h = std::stoi(sm[5]);
        }
        for (size_t i=x; i < x+w; i++)
            for (size_t j=y; j < y+h; j++)
                if (grid[i][j] > 1) {
                    remained_intact = false;
                    goto check;
                }
        check:
        if (remained_intact) {
            intact_id = id;
            break;
        }
    }
    std::cout << "Answer of part 2: " << intact_id << '\n';

    return 0;
}
