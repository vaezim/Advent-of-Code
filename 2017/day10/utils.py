class Round:
    def __init__(self, arr_size, lengths):
        self.curr = 0
        self.skip_size = 0
        self.lengths = lengths
        self.arr = list(range(arr_size))

    def Round(self):
        for length in self.lengths:
            end = (self.curr + length - 1) % len(self.arr)
            if length > 0:
                self._ReverseSublist(self.curr, end)
            self.curr = (self.curr + self.skip_size + length) % len(self.arr)
            self.skip_size += 1
    
    def Reset(self):
        self.arr = list(range(len(self.arr)))
        self.curr = 0
        self.skip_size = 0

    def _ReverseSublist(self, start, end):
        if start <= end:
            sublist = self.arr[start:end+1]
            sublist.reverse()
            for i in range(start,end+1):
                self.arr[i] = sublist[i-start]
        else:
            sublist = self.arr[start:] + self.arr[:end+1]
            sublist.reverse()
            for i in range(start,len(self.arr)):
                self.arr[i] = sublist[i-start]
            for i in range(end+1):
                self.arr[i] = sublist[len(self.arr)-start+i]
    

class KnotHash:
    def __init__(self, arr_size):
        self.arr_size = arr_size

    def RunRound(self, lengths, num=1):
        r = Round(self.arr_size, lengths)
        r.Reset()
        for _ in range(num):
            r.Round()
        return r.arr
    
    def GetHash(self, text):
        lengths = []
        # Ascii lengths
        for c in text:
            lengths.append(ord(c))
        lengths.extend([17, 31, 73, 47, 23])
        # 64 rounds of hash
        arr = self.RunRound(lengths, num=64)
        # XOR
        xor_list = []
        for i in range(16):
            sublist = arr[i*16:(i+1)*16]
            xor_list.append(self._ListXOR(sublist))
        # Hex representation
        hex_str = ""
        for n in xor_list:
            h = hex(n)[2:]
            if len(h) == 1:
                h = "0" + h
            hex_str += h
        return hex_str

    def _ListXOR(self, arr):
        res = arr[0]
        for i in range(1,len(arr)):
            res = res ^ arr[i]
        return res


if __name__ == "__main__":
    kh = KnotHash(256)
    tests = {"":            "a2582a3a0e66e6e86e3812dcb672a272",
             "AoC 2017":    "33efeb34ea91902bb2f59c9920caa6cd",
             "1,2,3":       "3efbe78a8d82f29979031a4aa0b16a9d",
             "1,2,4":       "63960835bcdc130f0b66d7ff4f6a5a8e"}
    for test in tests:
        if kh.GetHash(test) != tests[test]:
            print(f"[-] test {test} failed!")
        else:
            print(f"[+] Correct!")