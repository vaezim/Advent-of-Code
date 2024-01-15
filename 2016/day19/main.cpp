/*
 * https://www.youtube.com/watch?v=uCsD3ZGzMgE
 */

#include <string>
#include <iostream>
#include "linked_elves.h"

int main(int argc, char** argv) {

    // input
    int elfNum = 3017957;

    /*
     * Part 1
     */
    LinkedElves linkedElves(elfNum);
    int result = linkedElves.GetRemainingElf1();
    std::cout << "[+] Answer of part 1: " << result << '\n';

    /*
     * Part 2
     */
    result = linkedElves.GetRemainingElf2();
    std::cout << "[+] Answer of part 2: " << result << '\n';

    return 0;
}