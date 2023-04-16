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
    std::string walks;
    std::getline(file, walks);
    std::istringstream iss(walks);

    /*
     * Part 1
     */
    std::string walk;
    int x=0, y=0, walk_size;
    std::vector<std::array<int,2>> directions = {{0,1}, {1,0}, {0,-1}, {-1,0}}; // Up, Right, Down, Left
    size_t curr_dir = 0; // Up
    while (iss >> walk) {
        // remove ',' at the end
        if (*(walk.end()-1) == ',')
            walk = walk.substr(0,walk.length()-1);
        // change direction of movement
        if (walk[0] == 'R')
            curr_dir = (curr_dir+1) % directions.size();
        else if (walk[0] == 'L')
            curr_dir = (curr_dir-1) % directions.size();
        // walk in that direction
        walk_size = std::stoi(walk.substr(1));
        x += directions[curr_dir][0] * walk_size;
        y += directions[curr_dir][1] * walk_size;
    }
    std::cout << "Answer of part 1: " << (std::abs(x) + std::abs(y)) << '\n';

    /*
     * Part 2
     */
    const size_t map_len = 300;
    int map[map_len][map_len] = {0};
    x = (size_t)map_len/2; y = (size_t)map_len/2; curr_dir = 0;
    map[x][y] = 1;
    bool found_duplicate = false;
    while (true) {
        iss.clear();
        iss.str(walks);

        while (iss >> walk) {
            // remove ',' at the end
            if (*(walk.end()-1) == ',')
                walk = walk.substr(0,walk.length()-1);
            // change direction of movement
            if (walk[0] == 'R')
                curr_dir = (curr_dir+1) % directions.size();
            else if (walk[0] == 'L')
                curr_dir = (curr_dir-1) % directions.size();
            // walk in that direction
            walk_size = std::stoi(walk.substr(1));
            for (size_t i=0; i < walk_size; i++) {
                x += directions[curr_dir][0];
                y += directions[curr_dir][1];
                // check if it was visited
                if (map[x][y]) {
                    found_duplicate = true;
                    goto part2result;
                }
                // save the visited places
                map[x][y] = 1;
            }
        }
    }
    part2result:
    std::cout << "Answer of part 2: " << (std::abs(x-(int)map_len/2) + std::abs(y-(int)map_len/2)) << '\n';


    return 0;
}
