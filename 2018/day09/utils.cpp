#include "utils.h"
#include <iostream>
#include <algorithm>

Marbles::Marbles(size_t numPlayers, size_t numMarbles) :
    m_numPlayers(numPlayers), m_numMarbles(numMarbles)
{
    m_head = std::make_shared<Marble>(0);
    m_head->next = m_head;
    m_head->prev = m_head;
    m_players.resize(m_numPlayers, 0);
    BuildList();
}

void Marbles::BuildList()
{
    auto curr = m_head;
    for (uint32_t i{ 1 }; i < m_numMarbles; i++) {
        auto new_marble = std::make_shared<Marble>(i);
        uint32_t score = PlaceNewMarble(new_marble, curr);
        m_players[static_cast<size_t>(i % m_numPlayers)] += score;
    }
}

uint32_t Marbles::PlaceNewMarble(
    std::shared_ptr<Marble> &new_marble, 
    std::shared_ptr<Marble> &curr) const
{
    uint32_t score{ 0 };
    if (new_marble->score % 23 != 0) {
        // Place new marble between the 1st and 2nd next marbles
        auto m1 = curr->next;
        auto m2 = m1->next;
        m1->next = new_marble;
        m2->prev = new_marble;
        new_marble->prev = m1;
        new_marble->next = m2;
        // Set curr to new marble
        curr = new_marble;
    } else {
        for (uint8_t i{ 0 }; i < 7; i++) {
            curr = curr->prev;
        }
        score += new_marble->score;
        score += curr->score;
        auto left = curr->prev;
        auto right = curr->next;
        left->next = right;
        right->prev = left;
        curr->prev = nullptr;
        curr->next = nullptr;
        curr = right;
    }
    return score;
}

uint32_t Marbles::GetHighestScore()
{
    return *std::max_element(m_players.begin(), m_players.end());
}

void Marbles::Display() const
{
    auto curr = m_head;
    unsigned num23Marbles = m_numMarbles / 23;
    for (uint32_t i{ 0 }; i < m_numMarbles - num23Marbles*2; i++) {
        std::cout << curr->score << ", ";
        curr = curr->next;
    }
    std::cout << std::endl;
}