#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
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
        std::cout << "Unable to open " << FILENAME << '\n';
        return 1;
    }
    std::vector<std::string> presents;
    std::string present;
    while (std::getline(file, present)) {
        presents.push_back(present);
    }

    /*
     * Part 1
     */
    std::istringstream iss;
    std::string dim;
    int dimensions[3], areas[3], paper=0;
    for (const std::string& present: presents) {
        iss.str(present); iss.clear(); // clear() to reset the status bits including EOF flags
        for (size_t i=0; i < 3; i++) {
            std::getline(iss, dim, 'x');
            dimensions[i] = std::stoi(dim);
        }

        areas[0] = dimensions[0]*dimensions[1];
        areas[1] = dimensions[0]*dimensions[2];
        areas[2] = dimensions[1]*dimensions[2];
        paper += 2*(areas[0] + areas[1] + areas[2]);
        paper += *std::min_element(areas, areas+3); // areas.end() --> &areas[3] which does not exist.
    }
    std::cout << "Answer of part 1: " << paper << '\n';

    /*
     * Part 2
     */
    paper = 0;
    for (const std::string& present: presents) {
        iss.str(present); iss.clear(); // clear() to reset the status bits including EOF flags
        for (size_t i=0; i < 3; i++) {
            std::getline(iss, dim, 'x');
            dimensions[i] = std::stoi(dim);
        }

        paper += (dimensions[0] * dimensions[1] * dimensions[2]);
        paper += 2*(std::accumulate(dimensions, dimensions+3, 0) -
                    *std::max_element(dimensions, dimensions+3));
    }
    std::cout << "Answer of part 2: " << paper << '\n';

    return 0;
}
