#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <cmath>
#include <map>

#define ARR_LEN 50000
#define print(X) std::cout << X << '\n'
void update_grid(int** grid, const std::string& dir, unsigned& X, unsigned& Y,
                 std::vector<std::pair<unsigned,unsigned>>& intersects, unsigned wire_id);
unsigned min_wire_steps(const std::vector<std::string>& wires, int** grid);
unsigned manhattan_dist(int, int, int, int);

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
    std::vector<std::string> wires;
    while (std::getline(file, line)) {
        wires.push_back(line);
    }

    /*
     * Part 1
     */
    int** grid = new int*[ARR_LEN]; // static allocation won't go beyond 1Mb!
    for (unsigned i=0; i < ARR_LEN; i++)
        grid[i] = new int[ARR_LEN];
    std::istringstream iss;
    std::string dir;
    unsigned X, Y, wire_id=0;
    std::vector<std::pair<unsigned,unsigned>> intersects;
    for (const std::string& wire : wires) {
        wire_id++;
        X = (unsigned)ARR_LEN/2;
        Y = (unsigned)ARR_LEN/2;
        iss.str(wire); iss.clear();
        while (std::getline(iss, dir, ',')) {
            update_grid(grid, dir, X, Y, intersects, wire_id);
        }
    }
    unsigned min_dist = 2*ARR_LEN;
    for (const auto& pair : intersects) {
        min_dist = std::min(min_dist, manhattan_dist((unsigned)ARR_LEN/2,
                                                     (unsigned)ARR_LEN/2,
                                                     pair.first,
                                                     pair.second));
    }
    std::cout << "Answer of part 1: " << min_dist << '\n';

    /*
     * Part 2
     */
    unsigned min_total_steps = min_wire_steps(wires, grid);
    std::cout << "Answer of part 2: " << min_total_steps << '\n';

    for (unsigned i=0; i < ARR_LEN; i++)
        delete[] grid[i];
    delete[] grid;

    return 0;
}

void update_grid(int** grid, const std::string& dir, unsigned& X, unsigned& Y,
                 std::vector<std::pair<unsigned,unsigned>>& intersects, unsigned wire_id) {
    char direction = dir[0];
    int size = std::stoi(dir.substr(1));
    switch (direction) {
    case 'U':
        for (unsigned i=X+1; i <= X+size; i++) {
            if (grid[i][Y] == 0)
                grid[i][Y] = wire_id;
            else if (grid[i][Y] != wire_id && grid[i][Y] != -1) {
                grid[i][Y] = -1;
                intersects.push_back(std::make_pair(i,Y));
            }
        }
        X += size;
        break;
    case 'D':
        for (unsigned i=X-1; i >= X-size; i--) {
            if (grid[i][Y] == 0)
                grid[i][Y] = wire_id;
            else if (grid[i][Y] != wire_id && grid[i][Y] != -1) {
                grid[i][Y] = -1;
                intersects.push_back(std::make_pair(i,Y));
            }
        }
        X -= size;
        break;
    case 'R':
        for (unsigned j=Y+1; j <= Y+size; j++) {
            if (grid[X][j] == 0)
                grid[X][j] = wire_id;
            else if (grid[X][j] != wire_id && grid[X][j] != -1) {
                grid[X][j] = -1;
                intersects.push_back(std::make_pair(X,j));
            }
        }
        Y += size;
        break;
    case 'L':
        for (unsigned j=Y-1; j >= Y-size; j--) {
            if (grid[X][j] == 0)
                grid[X][j] = wire_id;
            else if (grid[X][j] != wire_id && grid[X][j] != -1) {
                grid[X][j] = -1;
                intersects.push_back(std::make_pair(X,j));
            }
        }
        Y -= size;
        break;
    }
}

unsigned min_wire_steps(const std::vector<std::string>& wires, int** grid) {
    
    std::istringstream iss;
    std::string dir;
    unsigned X, Y, wire_id=-1;
    unsigned steps[2] = {0,0};
    std::vector<std::map<std::pair<unsigned,unsigned>,unsigned>> wires_steps(wires.size());

    for (const std::string& wire : wires) {
        wire_id++;
        X = (unsigned)ARR_LEN/2;
        Y = (unsigned)ARR_LEN/2;
        iss.str(wire); iss.clear();

        while (std::getline(iss, dir, ',')) {
            char direction = dir[0];
            unsigned size = std::stoi(dir.substr(1));
            switch (direction) {
            case 'U':
                for (unsigned i=X+1; i <= X+size; i++) {
                    steps[wire_id]++;
                    if (grid[i][Y] == -1) {
                        auto& wire = wires_steps[wire_id];
                        if (wire.find(std::make_pair(i,Y)) == wire.end()) {
                            wire.insert({std::make_pair(i,Y),steps[wire_id]});
                        }
                    }
                }
                X += size;
                break;
            case 'D':
                for (unsigned i=X-1; i >= X-size; i--) {
                    steps[wire_id]++;
                    if (grid[i][Y] == -1) {
                        auto& wire = wires_steps[wire_id];
                        if (wire.find(std::make_pair(i,Y)) == wire.end()) {
                            wire.insert({std::make_pair(i,Y),steps[wire_id]});
                        }
                    }
                }
                X -= size;
                break;
            case 'R':
                for (unsigned j=Y+1; j <= Y+size; j++) {
                    steps[wire_id]++;
                    if (grid[X][j] == -1) {
                        auto& wire = wires_steps[wire_id];
                        if (wire.find(std::make_pair(X,j)) == wire.end()) {
                            wire.insert({std::make_pair(X,j),steps[wire_id]});
                        }
                    }
                }
                Y += size;
                break;
            case 'L':
                for (unsigned j=Y-1; j >= Y-size; j--) {
                    steps[wire_id]++;
                    if (grid[X][j] == -1) {
                        auto& wire = wires_steps[wire_id];
                        if (wire.find(std::make_pair(X,j)) == wire.end()) {
                            wire.insert({std::make_pair(X,j),steps[wire_id]});
                        }
                    }
                }
                Y -= size;
                break;
            }
        }
    }

    std::vector<unsigned> total_steps;
    for (const auto& item: wires_steps[0]) {
        total_steps.push_back(wires_steps[0][item.first] + wires_steps[1][item.first]);
    }

    return *std::min_element(total_steps.begin(), total_steps.end());
}

unsigned manhattan_dist(int x1, int y1, int x2, int y2) {
    return std::abs(x2-x1) + std::abs(y2-y1);
}
