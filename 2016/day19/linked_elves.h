#include <memory>

class Node {
public:
    Node(int pos) : position(pos){};
    ~Node() = default;

    int position;
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
};