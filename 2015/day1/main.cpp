#include <iostream>
#include <fstream>
#include <string>


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
    std::string floors;
    std::getline(file, floors);

    /*
     * Part 1
     */
    int santa = 0;
    for (const char& c: floors) {
        if (c == '(')
            santa++;
        else if (c == ')')
            santa--;
        else
            continue;
    }
    std::cout << "Answer of part 1: " << santa << '\n';

    /*
     * Part 2
     */
    size_t basement;
    santa = 0;
    for (size_t i=0; i < floors.length(); i++) {
        char c = floors[i];
        if (c == '(')
            santa++;
        else if (c == ')')
            santa--;
        
        if (santa == -1) {
            basement = i+1;
            break;
        }
    }
    std::cout << "Answer of part 2: " << basement << '\n';


    return 0;
}
