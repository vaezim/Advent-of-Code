
def IsNice1(s: str):
    s = s.strip()

    # rule 1
    char_map = {}
    for c in s:
        if char_map.get(c) == None:
            char_map[c] = 0
        char_map[c] += 1
    vowels = "aeiou"
    vowel_count = 0
    for v in vowels:
        if char_map.get(v):
            vowel_count += char_map[v]
    if vowel_count < 3:
        return False
    
    # rule 2
    rule2_passed = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            rule2_passed = True
            break
    if not rule2_passed:
        return False
    
    # rule 3
    substrs = ["ab", "cd", "pq", "xy"]
    for sub in substrs:
        if s.find(sub) != -1:
            return False
        
    return True

def IsNice2(s: str):
    s = s.strip()

    # rule 1
    rule1_passed = False
    for i in range(len(s)-1):
        if s[i+2:].find(s[i:i+2]) != -1:
            rule1_passed = True
            break
    if not rule1_passed:
        return False
    
    # rule 2
    rule2_passed = False
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            rule2_passed = True
    if not rule2_passed:
        return False
    
    return True

if __name__ == "__main__":
    print(IsNice1("ugknbfddgicrmopn"))
    print(IsNice1("aaa"))
    print(IsNice1("jchzalrnumimnmhp"))
    print(IsNice1("haegwjzuvuyypxyu"))
    print(IsNice1("dvszwmarrgswjxmb"))
