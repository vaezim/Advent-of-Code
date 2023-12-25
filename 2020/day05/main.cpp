#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int binaryString2int(std::string);

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
    int max_seatID = 0;
    for (const std::string& seat: lines)
        max_seatID = std::max(max_seatID, binaryString2int(seat));
    std::cout << "Answer of Part 1: " << max_seatID << '\n';

    /*
     * Part 2
     */
    std::vector<uint16_t> seats(1000);
    for (const std::string& seat: lines)
        seats[binaryString2int(seat)-1] = 1;

    size_t ptr = 0; // ptr to the first element in seats
    while (seats[ptr] == 0) // searching for the first nonzero seat
        ptr++;
    while (seats[ptr] == 1) // searching for a 0.
        ptr++;

    std::cout << "Answer of Part 2: " << ptr+1 << '\n';
    

    return 0;
}

int binaryString2int(std::string num) {
    for (size_t i=0; i < num.length(); i++) {
        if (num[i] == 'F' || num[i] == 'L')
            num[i] = '0';
        else if (num[i] == 'B' || num[i] == 'R')
            num[i] = '1';
        else
            return -1;
    }
    return std::stoi(num, 0, 2);
}
