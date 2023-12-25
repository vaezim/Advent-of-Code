#include <iostream>
#include <fstream>
#include <vector>
#include <string>

unsigned get_tree_count(const std::vector<std::string>&, const unsigned&, const unsigned&);

int main(int argc, char** argv) {
    /*
     * Reading File
     */
    if (argc != 2) {
        std::cout << "Usage: ./a.out [filename]\n";
        return 0;
    }
    std::string FILENAME = argv[1];
    std::ifstream file; file.open(FILENAME);
    if (!file.is_open()) {
        std::cout << "Unable to open " << FILENAME << '\n';
        return 0;
    }
    std::string line;
    std::vector<std::string> lines;
    while (std::getline(file, line))
        lines.push_back(line);

    /*
     * Part 1
     */
    unsigned right = 3, down = 1;
    std::cout << "Answer of part 1: " << get_tree_count(lines, right, down) << '\n';

    /*
     * Part 2
     */
    std::vector<unsigned> rights = {1, 3, 5, 7, 1};
    std::vector<unsigned> downs =  {1, 1, 1, 1, 2};
    unsigned multiple_tree_count = 1;
    for (size_t i=0; i < rights.size(); i++)
        multiple_tree_count *= get_tree_count(lines, rights[i], downs[i]);
    std::cout << "Answer of part 2: " << multiple_tree_count << '\n';

    return 0;
}

unsigned get_tree_count(const std::vector<std::string>& lines, const unsigned& right, const unsigned& down) {
    unsigned tree_count = 0;
    unsigned Y = 0, Y_len = lines[0].length();
    std::string line;
    for (size_t X=0; X < lines.size(); X+=down) {
        line = lines[X];
        tree_count += (line[Y] == '#');
        Y = (Y + right) % Y_len;
    }
    return tree_count;
}