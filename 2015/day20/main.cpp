#include "utils.h"


int main(int argc, char** argv) {

    ul64 input = 36000000;

    /*
     * Part 1
     */
    ul64 result = GetMinNumWithMaxSumDivisors1(input);
    std::cout << "[+] Answer of part 1: " << result << "\n\n";

    /*
     * Part 2
     */
    result = GetMinNumWithMaxSumDivisors2(input);
    std::cout << "[+] Answer of part 2: " << result << '\n';

    return 0;
}
