#include <cmath>
#include <iostream>
#include "linked_elves.h"

void LinkedElves::CreateLinkedElves()
{
    m_head = std::make_shared<Node>(1);
    std::shared_ptr<Node> curr = m_head;
    for (int i=2; i <= m_elfNum; i++) {
        auto next = std::make_shared<Node>(i);
        curr->next = next;
        curr = next;
    }
    curr->next = m_head;
}

int LinkedElves::GetRemainingElf1()
{
    int left_elves = m_elfNum;
    std::shared_ptr<Node> curr = m_head;
    while (left_elves > 1) {
        auto next_node = curr->next->next;
        curr->next = next_node;
        curr = next_node;
        left_elves--;
    }
    return curr->position;
}

int LinkedElves::GetRemainingElf2()
{
    int last_turn_winner = 3;  // winner at elf_num = 3
    for (int elf_num=4; elf_num <= m_elfNum; elf_num++) {
        int next = 2;
        int removed_element = std::floor(elf_num/2.0) + 1;
        int dist_to_removed = (next <= removed_element) ?
            removed_element - next :
            removed_element + elf_num - next;
        int winner = (last_turn_winner - 1 < dist_to_removed) ?
            next + last_turn_winner - 1 :
            next + last_turn_winner;
        if (winner > elf_num) {
            winner -= elf_num;
        }
        last_turn_winner = winner;
    }
    return last_turn_winner;
}