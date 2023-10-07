#pragma once
#include <string>
#include <memory>


class Monkey {
public:
    explicit Monkey(const std::string& name) : 
        m_name(name) {};
    
    void AddNum(const long long num) {
        m_num = num;
    }
    void AddChildren(std::shared_ptr<Monkey> left, std::shared_ptr<Monkey> right, char op) {
        m_left = left;
        m_right = right;
        m_op = op;
    }
    long long Resolve() {
        if (!m_left && !m_right)
            return m_num;
        auto left_num = m_left->Resolve();
        auto right_num = m_right->Resolve();
        m_left = nullptr; m_right = nullptr;

        switch (m_op) {
            case '+':
                m_num = left_num + right_num;
                break;
            case '-':
                m_num = left_num - right_num;
                break;
            case '*':
                m_num = left_num * right_num;
                break;
            case '/':
                m_num = (long long)(left_num / right_num);
                break;
            default:
                return -999;
        }

        return m_num;
    }
    bool Equality() {
        return m_left->Resolve() == m_right->Resolve();
    }

public:
    std::string m_name;
    long long m_num = -999;
    char m_op = '!';
    std::shared_ptr<Monkey> m_left = nullptr;
    std::shared_ptr<Monkey> m_right = nullptr;

};
