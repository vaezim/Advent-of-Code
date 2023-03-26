#include <unordered_map>
#include <unordered_set>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <set>

bool verify_passport1(const std::string&);
bool verify_passport2(const std::string&);

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
    lines.push_back("\n");

    /*
     * Part 1
     */
    unsigned valid_count1 = 0, valid_count2 = 0, passport_count = 0;
    std::string passport = "";
    for (size_t i=0; i < lines.size(); i++) {
        if (lines[i].length() <= 1) { // "" or "\n"
            passport_count++;
            valid_count1 += verify_passport1(passport); // part 1
            valid_count2 += verify_passport2(passport); // part 2
            passport = "";
        } else {
            passport += " ";
            passport += lines[i];
        }
    }
    std::cout << "Answer of part 1: " << valid_count1 << '/' << passport_count << '\n';

    /*
     * Part 2
     */
    std::cout << "Answer of part 2: " << valid_count2 << '/' << passport_count << '\n';

    return 0;
}

bool verify_passport1(const std::string& passport) {
    const static std::set<std::string> valid_fields = { 
        "byr", "iyr", "eyr", "hgt",
        "hcl", "ecl", "pid", "cid"
    };
    std::istringstream iss(passport);
    std::string token;
    std::set<std::string> passport_fields = {"cid"}; // optional

    while (std::getline(iss, token, ' ')) {
        if (token.length())
            passport_fields.insert(
                token.substr(0,token.find(':')));
    }

    return passport_fields == valid_fields;
}

bool verify_passport2(const std::string& passport) {
    const static std::vector<std::string> valid_fields = {
        "byr", "iyr", "eyr", "hgt",
        "hcl", "ecl", "pid", "cid"
    };
    std::istringstream iss(passport);
    std::string token;
    std::unordered_map<std::string, std::string> passport_fields = {{"cid",""}}; // optional

    while (std::getline(iss, token, ' ')) {
        if (token.length())
            passport_fields[token.substr(0,token.find(':'))] = 
                token.substr(token.find(':')+1);
    }

    // all present
    if (passport_fields.size() < 8)
        return false;
    // birthday
    int birthday = std::stoi(passport_fields["byr"]);
    if (passport_fields["byr"].length() != 4 || birthday < 1920 || birthday > 2002)
        return false;
    // issue year
    int issue_year = std::stoi(passport_fields["iyr"]);
    if (passport_fields["iyr"].length() != 4 || issue_year < 2010 || issue_year > 2020)
        return false;
    // expire date
    int expire_date = std::stoi(passport_fields["eyr"]);
    if (passport_fields["eyr"].length() != 4 || expire_date < 2020 || expire_date > 2030)
        return false;
    // height
    int height = std::stoi(passport_fields["hgt"]);
    std::string unit = passport_fields["hgt"].substr(passport_fields["hgt"].length()-2);
    if (unit == "cm") {
        if (height < 150 || height > 193)
            return false;
    } else if (unit == "in") {
        if (height < 59 || height > 76)
            return false;
    } else
    return false;
    // hair color
    std::string hair_color = passport_fields["hcl"];
    if (hair_color.length() != 7)
        return false;
    // eye color
    std::unordered_set<std::string> eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
    std::string eye_color = passport_fields["ecl"];
    if (!eye_colors.count(eye_color))
        return false;
    // passport ID
    std::string pid = passport_fields["pid"];
    if (pid.length() != 9)
        return false;

    return true;
}
