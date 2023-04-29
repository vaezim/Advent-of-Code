#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>

size_t getNumHouses(const std::string& line, 
                    std::set<std::pair<size_t,size_t>>&,
                    size_t offset=0, 
                    size_t step=1);

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

    /*
     * Part 1
     */
    std::set<std::pair<size_t,size_t>> places1;
    std::cout << "Answer of part 1: " << getNumHouses(line,places1) << '\n';

    /*
     * Part 2
     */
    std::set<std::pair<size_t,size_t>> places2;
    getNumHouses(line,places2,0,2); // Let Santa finish his walk ;)
    std::cout << "Answer of part 2: " << getNumHouses(line,places2,1,2) << '\n';

    return 0;
}

size_t getNumHouses(const std::string& line,
                    std::set<std::pair<size_t,size_t>>& places,
                    size_t offset, 
                    size_t step) {
    std::pair<size_t,size_t> curr_loc;
    curr_loc.first = 0; curr_loc.second = 0;
    places.insert(curr_loc);
    char c;

    for (size_t i=offset; i < line.length(); i+=step) {
        c = line[i];
        if (c == '^')
            curr_loc.second++;
        else if (c == 'v')
            curr_loc.second--;
        else if (c == '<')
            curr_loc.first--;
        else if (c == '>')
            curr_loc.first++;
        places.insert(curr_loc);
    }

    return places.size();
}
