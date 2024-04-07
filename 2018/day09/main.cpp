#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>

#include "utils.h"

int main(int argc, char** argv) {

    /*
     * Input
     */
    size_t num_players = 459;
    size_t num_marbles = 71790 + 1;

    /*
     * Part 1
     */
    Marbles marbles(num_players, num_marbles);
    auto res = marbles.GetHighestScore();
    std::cout << "[+] Answer of part 1: " << res << '\n';

    /*
     * Part 2
     */
    num_marbles = 100 * 71790 + 1;
    marbles = Marbles(num_players, num_marbles);
    res = marbles.GetHighestScore();
    std::cout << "[+] Answer of part 2: " << res << '\n';
    return 0;
}