
def NextLookSayNum(n: str) -> str:
    res = ""
    cnt = 0
    curr = n[0]
    for c in n:
        if c == curr:
            cnt += 1
            continue
        res += f"{cnt}{curr}"
        curr = c
        cnt = 1
    res += f"{cnt}{curr}"
    return res

if __name__ == "__main__":
    print(NextLookSayNum("1"))
    print(NextLookSayNum("11"))
    print(NextLookSayNum("11112224"))
    print(NextLookSayNum("123"))
    