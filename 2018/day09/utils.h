#include <vector>
#include <memory>
#include <cstdint>
#include <cstddef>

class Marble {
public:
    Marble(uint32_t score) : score(score) {}
    ~Marble() = default;

    uint32_t score;
    std::shared_ptr<Marble> next{ nullptr };
    std::shared_ptr<Marble> prev{ nullptr };
};

class Marbles {
public:
    Marbles(size_t numPlayers, size_t numMarbles);
    ~Marbles() = default;

    void Display() const;
    uint32_t GetHighestScore();

private:
    size_t m_numPlayers;
    size_t m_numMarbles;
    std::shared_ptr<Marble> m_head;
    std::vector<uint32_t> m_players;

    void BuildList();
    uint32_t PlaceNewMarble(
        std::shared_ptr<Marble> &new_marble, 
        std::shared_ptr<Marble> &curr) const;
};