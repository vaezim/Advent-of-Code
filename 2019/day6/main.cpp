#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include "planet.cpp"

using PlanetMap = std::unordered_map<std::string, std::shared_ptr<Planet>>;

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
    std::string line;
    std::vector<std::string> lines;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    /*
     * Part 1
     */
    PlanetMap planets;
    for (const std::string& line: lines) {
        // Get names
        size_t seperator = line.find(')');
        std::string name1, name2;
        name1 = line.substr(0,seperator);
        name2 = line.substr(seperator+1);

        // Planet pointers
        std::shared_ptr<Planet> p1;
        std::shared_ptr<Planet> p2;

        // Add to [planets] hashmap
        if (!planets.count(name1)) {
            p1 = std::make_shared<Planet>(name1);
            planets.insert({name1, p1});
        }
        if (!planets.count(name2)) {
            p2 = std::make_shared<Planet>(name2);
            planets.insert({name2, p2});
        }

        // Add parent and child
        p1 = planets[name1];
        p2 = planets[name2];
        p2->AddParent(p1);
        p1->AddChild(p2);
    }
    uint32_t sum_distances = 0;
    for (const auto& planet: planets) {
        sum_distances += planet.second->GetDistanceToCOM();
    }
    std::cout << "Answer of part 1: " << sum_distances << '\n';

    /*
     * Part 2
     */
    std::unordered_set<const Planet*> visited;
    auto YOU = planets.find("YOU")->second;
    if (!YOU) {
        std::cout << "Could not find the YOU planet!\n";
        return 1;
    }
    uint32_t YOU2SANdist = YOU->GetDistanceToSAN(visited);
    std::cout << "Answer of part 2: " << YOU2SANdist - 2 << '\n';

    return 0;
}
