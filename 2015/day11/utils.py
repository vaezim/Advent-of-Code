
def IsValidPassword(s: str) -> bool:

    # rule 1
    rule1 = False
    n = list(map(lambda x: ord(x), list(s)))
    for i in range(len(n)-2):
        if n[i] == n[i+1] - 1 and n[i+1] == n[i+2] - 1:
            rule1 = True
            break
    if not rule1:
        return False
    
    # rule 2
    restricted_letters = "iol"
    for c in s:
        if c in restricted_letters:
            return False
    
    # rule 3
    first_pair = ""
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            if len(first_pair) == 0:
                first_pair = s[i:i+2]
            else:
                if s[i:i+2] != first_pair:
                    return True
    
    return False

def NextPassword(s: str) -> str:
    n = list(map(lambda x: ord(x), list(s)))
    for i in range(len(n)-1,-1,-1):
        if n[i] < ord('z'):
            n[i] += 1
            break
        n[i] = ord('a')
    return ''.join(list(map(lambda x: chr(x), n)))

if __name__ == "__main__":
    print(IsValidPassword("hijklmmn"))
    print(IsValidPassword("abbceffg"))
    print(IsValidPassword("abbcegjk"))
    print(IsValidPassword("abcdffaa"))
    print(IsValidPassword("ghjaabcc"))

    print(NextPassword("yx"))
    print(NextPassword("yy"))
    print(NextPassword("yz"))
    print(NextPassword("ghijklmn"))
    print(NextPassword("ghijklzz"))
