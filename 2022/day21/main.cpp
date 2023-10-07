#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <string>
#include <vector>
#include "Monkey.cpp"


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
        throw std::runtime_error("Unable to open file " + FILENAME);
    }
    std::string line, word;
    std::vector<std::string> lines, words;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    /*
     * Part 1
     */
    std::shared_ptr<Monkey> monk;
    std::unordered_map<std::string, std::shared_ptr<Monkey>> monkeys;
    std::istringstream iss;

    for (const std::string& line: lines) {
        iss.str(line); iss.clear();
        iss >> word;
        word = word.substr(0, word.length()-1);
        monk = std::make_shared<Monkey>(word);
        monkeys.insert({word, monk});
    }

    for (const std::string& line: lines) {
        iss.str(line); iss.clear();
        while (std::getline(iss, word, ' ')) {
            words.push_back(word);
        }
        word = words[0].substr(0, words[0].length()-1); // name
        monk = monkeys.find(word)->second;
        if (words.size() == 2) {
            monk->AddNum(std::stoi(words[1]));
        } else {
            char op = words[2][0];
            monk->AddChildren(monkeys.find(words[1])->second,
                              monkeys.find(words[3])->second, op);
        }
        words.clear();
    }

    monk = monkeys.find("root")->second;
    long long right_num = monk->m_right->Resolve();
    std::cout << "Answer of part 1: " << monk->Resolve() << '\n';

    /*
     * Part 2 (BRUTAL!)
     */

    std::cout << "Right: " << right_num << '\n';
    long long left_num;
    long long human_num;
    long long CEIL = 3'580'000'000'000, ROOF = 3'590'000'000'000;
    long long i = (long long)((CEIL + ROOF)/2);
    while (true) {

        // reset monkeys
        for (const std::string& line: lines) {
            iss.str(line); iss.clear();
            while (std::getline(iss, word, ' ')) {
                words.push_back(word);
            }
            word = words[0].substr(0, words[0].length()-1); // name
            monk = monkeys.find(word)->second;
            if (words.size() == 2) {
                monk->AddNum(std::stoi(words[1]));
            } else {
                char op = words[2][0];
                monk->AddChildren(monkeys.find(words[1])->second,
                                monkeys.find(words[3])->second, op);
            }
            words.clear();
        }
        
        // find human
        std::shared_ptr<Monkey> human;
        for (auto& monk: monkeys) {
            if (monk.first == "humn") {
                human = monk.second;
                break;
            }
        }
        if (!human)
            throw std::runtime_error("Human monkey not found!\n");
        human->AddNum(i);

        monk = monkeys.find("root")->second;
        left_num = monk->m_left->Resolve();
        if (right_num-left_num < ) {
            
        }
    }
    
    std::cout << "Answer of part 2: " << human_num << '\n';

    return 0;
}
