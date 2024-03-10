#include "utils.h"
#include <iostream>

Pins::Pins(const std::vector<std::string> &lines) : m_lines(lines)
{
    ParseLines();
}

void Pins::ParseLines()
{
    for (const auto &line : m_lines) {
        size_t slashIdx = line.find('/');
        uint16_t side1 = std::stoi(line.substr(0, slashIdx));
        uint16_t side2 = std::stoi(line.substr(slashIdx+1));
        m_pins.insert(Pin{ side1, side2 });
    }
}

uint32_t Pins::GetStrongestBridge() const
{
    PinSet pins = m_pins;
    /* Get pins with a zero side */
    PinSet candidates;
    for (const auto &item : pins) {
        if (item.side1 == 0 || item.side2 == 0) {
            candidates.insert(item);
        }
    }
    /* Start a subtree for each zero-sided candidate */
    for (const auto &item : candidates) {
        pins.erase(item);
        uint16_t lastPinSide = (item.side1 == 0) ? item.side2 : item.side1;
        GetStrongestBridge(lastPinSide, pins, item.side1 + item.side2);
        pins.insert(item);
    }
    return m_maxSum;
}

void Pins::GetStrongestBridge(const uint16_t &lastPinSide, PinSet &pins, uint32_t sum) const
{
    /* Get candidates for the next pin */
    PinSet candidates;
    for (const auto &item : pins) {
        if (lastPinSide == item.side1 || lastPinSide == item.side2) {
            candidates.insert(item);
        }
    }
    /* Base case */
    if (candidates.size() == 0) {
        m_maxSum = std::max(m_maxSum, sum);
        return;
    }
    /* Try each candidate */
    for (const auto &item : candidates) {
        pins.erase(item);
        uint16_t nextPinSide = (item.side1 == lastPinSide) ? item.side2 : item.side1;
        GetStrongestBridge(nextPinSide, pins, sum + item.side1 + item.side2);
        pins.insert(item);
    }
}

uint32_t Pins::GetLongestBridge() const
{
    m_maxSum = 0;
    PinSet pins = m_pins;
    /* Get pins with a zero side */
    PinSet candidates;
    for (const auto &item : pins) {
        if (item.side1 == 0 || item.side2 == 0) {
            candidates.insert(item);
        }
    }
    /* Start a subtree for each zero-sided candidate */
    for (const auto &item : candidates) {
        pins.erase(item);
        uint16_t lastPinSide = (item.side1 == 0) ? item.side2 : item.side1;
        GetLongestBridge(lastPinSide, pins, item.side1 + item.side2);
        pins.insert(item);
    }
    return m_maxSum;
}

void Pins::GetLongestBridge(const uint16_t &lastPinSide, PinSet &pins, uint32_t sum) const
{
    /* Get candidates for the next pin */
    PinSet candidates;
    for (const auto &item : pins) {
        if (lastPinSide == item.side1 || lastPinSide == item.side2) {
            candidates.insert(item);
        }
    }
    /* Base case */
    if (candidates.size() == 0) {
        uint32_t length = m_pins.size() - pins.size();
        if (length >= m_longest) {
            m_maxSum = std::max(m_maxSum, sum);
            m_longest = std::max(m_longest, length);
        }
        return;
    }
    /* Try each candidate */
    for (const auto &item : candidates) {
        pins.erase(item);
        uint16_t nextPinSide = (item.side1 == lastPinSide) ? item.side2 : item.side1;
        GetLongestBridge(nextPinSide, pins, sum + item.side1 + item.side2);
        pins.insert(item);
    }
}