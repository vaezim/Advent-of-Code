#include <iostream>
#include "linked_elves.h"

void LinkedElves::CreateLinkedElves()
{
    m_elves.reserve(m_elfNum);
    for (int i=0; i < m_elfNum; i++) {
        m_elves.push_back(std::make_shared<Node>(i+1));
    }
    for (int i=0; i < m_elfNum-1; i++) {
        m_elves[i]->next = m_elves[i+1];
        m_elves[i+1]->prev = m_elves[i];
    }
    m_elves[0]->prev = m_elves.back();
    m_elves.back()->next = m_elves[0];
    m_head = m_elves.front();
    m_tail = m_elves.back();
}

int LinkedElves::GetRemainingElf1()
{
    auto elfNum = m_elfNum;
    std::shared_ptr<Node> curr = m_head;
    while (elfNum > 1) {
        if (curr->val == 0) {
            std::shared_ptr<Node> p = curr->prev;
            std::shared_ptr<Node> n = curr->next;
            p->next = n;
            n->prev = p;

            curr->prev = nullptr;
            curr->next = nullptr;
            curr = n;
            elfNum--;
            continue;
        }
        if (curr->next == nullptr) {
            std::cout << "Elf number " << curr->position << " has no next\n";
            return -1;
        }
        curr->val += curr->next->val;
        curr->next->val = 0;
        curr = curr->next;
    }
    for (const auto &elf: m_elves) {
        if (elf->val > 0) {
            return elf->position;
        }
    }
    return -1;
}

int LinkedElves::GetRemainingElf2()
{
    
}