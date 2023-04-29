#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

bool isValidTriangle(const int&, const int&, const int&);

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
    std::istringstream iss;
    int a, b, c, valid_num=0;
    for (const std::string& line: lines) {
        iss.str(line); iss.clear();
        iss >> a >> b >> c;
        valid_num += isValidTriangle(a,b,c);
    }
    std::cout << "Answer of part 1: " << valid_num << '\n';

    /*
     * Part 2
     */
    valid_num=0;
    int triangles[3][3];
    std::vector<std::istringstream> streams(3);
    for (size_t i=0; i < lines.size(); i+=3) {
        for (size_t j=0; j < 3; j++) {
            streams[j].str(lines[i+j]); streams[j].clear();
            for (size_t t=0; t < 3; t++) {
                streams[j] >> triangles[t][j];
            }
        }
        for (size_t t=0; t < 3; t++)
            valid_num += isValidTriangle(triangles[t][0],triangles[t][1],triangles[t][2]);
    }
    std::cout << "Answer of part 2: " << valid_num << '\n';

    return 0;
}

bool isValidTriangle(const int& a, const int& b, const int& c) {
    return ((a+b > c) && (a+c > b) && (b+c > a));
}
