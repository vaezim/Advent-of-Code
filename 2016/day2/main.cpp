#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <array>
#include <cmath>


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
    std::vector<std::string> instructs;
    std::string instruct;
    while (std::getline(file, instruct)) {
        instructs.push_back(instruct);
    }

    /*
     * Part 1
     */
    int x=1, y=1; // initial position
    std::string password = "";
    for (const std::string& instruct: instructs) {
        for (const char& dir: instruct) {
            switch (dir) {
                case 'U':
                    x = std::max(0,x-1); break;
                case 'D':
                    x = std::min(2,x+1); break;
                case 'L':
                    y = std::max(0,y-1); break;
                case 'R':
                    y = std::min(2,y+1); break;
                default:
                    std::cout << "Invalid direction character!\n";
            }
        }
        password += std::to_string(x*3+y+1);
    }
    std::cout << "Answer of part 1: " << password << '\n';
    
    /*
     * Part 2
     */
    char keypad[5][6] = {"__1__", "_234_", "56789", "_ABC_", "__D__"};
    password = "";
    for (const std::string& instruct: instructs) {
        for (const char& dir: instruct) {
            switch (dir) {
                case 'U':
                    if (x > 0 && keypad[x-1][y] != '_')
                        x--;
                    break;
                case 'D':
                    if (x < 4 && keypad[x+1][y] != '_')
                        x++;
                    break;
                case 'L':
                    if (y > 0 && keypad[x][y-1] != '_')
                        y--;
                    break;
                case 'R':
                    if (y < 4 && keypad[x][y+1] != '_')
                        y++;
                    break;
                default:
                    std::cout << "Invalid direction character!\n";
            }
        }
        password += keypad[x][y];
    }
    std::cout << "Answer of part 2: " << password << '\n';

    return 0;
}
