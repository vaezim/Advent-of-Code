#include <vector>
#include <memory>

class Node {
public:
    Node(int pos) : val(1), position(pos){};
    ~Node() = default;

    int val;
    int position;
    std::shared_ptr<Node> prev {nullptr};
    std::shared_ptr<Node> next {nullptr};
};

class LinkedElves {
public:
    LinkedElves(int elfNum) : m_elfNum(elfNum) {
        CreateLinkedElves();
    }
    ~LinkedElves() = default;

    int GetRemainingElf1();
    int GetRemainingElf2();

private:
    void CreateLinkedElves();

    int m_elfNum;
    std::shared_ptr<Node> m_head {nullptr};
    std::shared_ptr<Node> m_tail {nullptr};
    std::vector<std::shared_ptr<Node>> m_elves;
};