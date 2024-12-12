#include <iostream>
#include <unordered_set>
#include "solver.h"


Solver::Solver(const std::string &line)
{
    m_nums.reserve(line.size());
    for (const auto &c : line) {
        m_nums.push_back(c - '0');
    }
}

uint64_t Solver::SolvePart1()
{
    // Generate filesystem
    size_t idx{ 0 };
    int currVal{ 0 };
    std::vector<int> filesystem(m_nums.size()*9, -1);
    for (size_t i{ 0 }; i < m_nums.size(); i++) {
        if (i % 2 == 1) {
            idx += m_nums[i];
            continue;
        }
        for (size_t j{ 0 }; j < m_nums[i]; j++) {
            filesystem[idx++] = currVal;
        }
        currVal++;
    }
    // Fill empty spots from the left with files from the right :/
    int l = 0;
    int r = filesystem.size()-1;
    while (r > l) {
        while (filesystem[l] != -1 && l < filesystem.size()) {
            l++;
        }
        while (filesystem[r] == -1 && r > 0) {
            r--;
        }
        if (l >= r) break;
        filesystem[l] = filesystem[r];
        filesystem[r] = -1;
    }
    // Calculate checksum
    uint64_t checksum{ 0 };
    for (int i{ 0 }; i < filesystem.size(); i++) {
        if (filesystem[i] == -1) break;
        checksum += i * filesystem[i];
    }
    return checksum;
}

uint64_t Solver::SolvePart2()
{
    // Generate filesystem
    size_t idx{ 0 };
    int currVal{ 0 };
    std::vector<int> filesystem(m_nums.size()*9, 0);
    std::vector<std::pair<size_t, int>> fileSegments;
    std::vector<std::pair<size_t, int>> emptySegments;
    for (size_t i{ 0 }; i < m_nums.size(); i++) {
        if (i % 2 == 1) {
            emptySegments.emplace_back(idx, m_nums[i]);
            idx += m_nums[i];
            continue;
        }
        fileSegments.emplace_back(idx, m_nums[i]);
        for (size_t j{ 0 }; j < m_nums[i]; j++) {
            filesystem[idx++] = currVal;
        }
        currVal++;
    }
    // Defragmentation
    for (size_t i{ fileSegments.size()-1 }; i > 0; i--) {
        size_t file_index = fileSegments[i].first;
        int file_size = fileSegments[i].second;
        for (size_t j{ 0 }; j < emptySegments.size(); j++) {
            size_t empty_index = emptySegments[j].first;
            int empty_size = emptySegments[j].second;
            if (file_index <= empty_index) break;
            if (empty_size < file_size) continue;
            for (size_t k{ 0 }; k < file_size; k++) {
                filesystem[empty_index+k] = filesystem[file_index+k];
                filesystem[file_index+k] = 0;
            }
            emptySegments[j].first += file_size;
            emptySegments[j].second -= file_size;
            break;
        }
    }
    // Calculate checksum
    uint64_t checksum{ 0 };
    for (int i{ 0 }; i < filesystem.size(); i++) {
        checksum += i * filesystem[i];
    }
    return checksum;
}