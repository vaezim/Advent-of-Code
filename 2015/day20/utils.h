#pragma once

#include <cmath>
#include <vector>
#include <utility>
#include <iostream>
#include <algorithm>

using ul64 = uint64_t;
using ppp = std::pair<ul64,ul64>;  // <prime, power> pair

std::vector<ul64> primes {2, 3, 5, 7};

void FillPrimes(ul64 end=1000) {
    std::cout << "Generating primes list...\n\n";
    for (ul64 i=primes.back()+1; i <= end; i++) {
        bool isPrime = true;
        for (const auto &p: primes) {
            if (p > std::sqrt(i)) { break; }
            if (i % p == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) { primes.push_back(i); }
    }
}

std::vector<ppp> GetPrimeFactors(ul64 n) {
    auto initial_n_2 = n/2;
    std::vector<ppp> primeFactors;
    for (auto p: primes) {
        ul64 power = 0;
        if (p > initial_n_2) { break; }
        if (n == 1) { break; }
        while (n % p == 0) {
            n = static_cast<ul64>(n / p);
            power++;
        }
        if (power > 0) {
            primeFactors.push_back({p, power});
        }
    }
    return std::move(primeFactors);
}

ul64 GetSumDivisors(const ul64 &n) {
    ul64 sum = 1;
    std::vector<ppp> primeFactors;
    primeFactors = GetPrimeFactors(n);
    if (primeFactors.size() == 0) { return 0; }
    for (const auto &pp: primeFactors) {
        auto p = pp.first;
        auto power = pp.second;
        sum *= static_cast<ul64>(
            (std::pow(p,power+1) - 1) / (p - 1));
    }
    return sum;
}

ul64 GetMinNumWithMaxSumDivisors1(ul64 max) {
    FillPrimes(1e6);
    ul64 i = 1;
    short giftPerHouse = 10;
    while (i > 0) {
        ul64 sumDivisors = GetSumDivisors(i) * giftPerHouse;
        if (sumDivisors >= max) {
            return i;
        }
        if (i % 100'000 == 0) {
            std::cout << "[*] Searched " << i << " numbers.\n";
        }
        i++;
    }
    return 0;
}

ul64 GetMinNumWithMaxSumDivisors2(ul64 max) {
    std::vector<ul64> houses(static_cast<size_t>(1e8), 0);
    ul64 i = 1;
    while (i < houses.size()/50) {
        for (short j=1; j<=50; j++) {
            houses[i*j] += static_cast<ul64>(i*11);
        }
        i++;
    }
    ul64 minMaxHouseIndex = 0;
    while (houses[minMaxHouseIndex] < max) {
        minMaxHouseIndex++;
    }
    return minMaxHouseIndex;
}

void DispVector(const std::vector<ul64> &v) {
    for (const auto &i: v) {
        std::cout << i << ", ";
    }
    std::cout << '\n';
}

void DispVector(const std::vector<ppp> &v) {
    for (const auto &i: v) {
        std::cout << "(" << i.first << ", " << i.second << ")" << '\n';
    }
    std::cout << '\n';
}
