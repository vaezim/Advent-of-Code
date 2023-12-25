#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

#define print(x) std::cout << x << '\n'
size_t get_neighbor_sum(size_t g[600][600], size_t x, size_t y);

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
    std::getline(file, line);
    int target = std::stoi(line);

    /*
     * Part 1
     */
    int square_len=1;
    while (std::pow(square_len,2) < target)
        square_len += 2;
    int square_half_len = (int)((square_len-1)/2);

    int square_corner = std::pow(square_len,2);
    int centers[4] = {std::abs(target-(square_corner-square_half_len)),
                      std::abs(target-(square_corner-3*square_half_len)),
                      std::abs(target-(square_corner-5*square_half_len)),
                      std::abs(target-(square_corner-7*square_half_len))};

    size_t manhattan = square_half_len;
    manhattan += *std::min_element(centers, centers+3);
    std::cout << "Answer of part 1: " << manhattan << '\n';

    /*
     * Part 2
     */
    size_t grid[600][600] = {};
    size_t x=300, y=300;
    grid[x][y] = 1;

    square_len = 1;
    size_t curr_len = 0, repeats = 0;

    enum class DIRECTION {RIGHT, UP, LEFT, DOWN};
    DIRECTION curr_dir = DIRECTION::RIGHT;

    while (grid[x][y] <= target) {
        if (curr_len == square_len && repeats == 0) {
            repeats++;
            curr_dir = (DIRECTION)(((size_t)curr_dir + 1) % 4);
            curr_len = 0;
            continue;
        }
        if (curr_len == square_len && repeats == 1) {
            repeats = 0;
            curr_dir = (DIRECTION)(((size_t)curr_dir + 1) % 4);
            curr_len = 0;
            square_len++;
            continue;
        }
        
        switch (curr_dir) {
            case DIRECTION::RIGHT:
                y++;
                grid[x][y] = get_neighbor_sum(grid, x, y);
                break;
            case DIRECTION::LEFT:
                y--;
                grid[x][y] = get_neighbor_sum(grid, x, y);
                break;
            case DIRECTION::UP:
                x++;
                grid[x][y] = get_neighbor_sum(grid, x, y);
                break;
            case DIRECTION::DOWN:
                x--;
                grid[x][y] = get_neighbor_sum(grid, x, y);
                break;
        }
        curr_len++;
    }
    
    std::cout << "Answer of part 2: " << grid[x][y] << '\n';

    return 0;
}

size_t get_neighbor_sum(size_t g[600][600], size_t x, size_t y) {
    return (g[x+1][y] + 
            g[x][y+1] + 
            g[x+1][y+1] +
            g[x-1][y] + 
            g[x-1][y-1] +
            g[x][y-1] + 
            g[x+1][y-1] + 
            g[x-1][y+1]);
}
