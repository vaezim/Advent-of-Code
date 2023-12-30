class HashMap:
    def __init__(self, line):
        self.line = line
        self.boxes = [[] for _ in range(256)]

    def GetSumLineHash(self):
        sum = 0
        words = self.line.strip().split(",")
        for w in words:
            sum += self._Hash(w)
        return sum

    def GetBoxesFocusPower(self):
        res = 0
        self._BuildLensBoxes()
        for box_index in range(256):
            res += self._GetBoxFocusPower(box_index)
        return res

    def _GetBoxFocusPower(self, box_index):
        sum = 0
        box = self.boxes[box_index]
        for slot, lens in enumerate(box):
            sum += (box_index + 1) * (slot + 1) * lens[1]
        return sum

    def _BuildLensBoxes(self):
        for lop in self._GetLabelOperations():
            label, op, focal_num = lop
            box_index = self._Hash(label)
            lens_index = self._FindLensInBox(box_index, label)
            if op == "=":
                if lens_index == -1:
                    self.boxes[box_index].append([label, focal_num])
                else:
                    self.boxes[box_index][lens_index][1] = focal_num
            elif op == "-" and lens_index != -1:
                self.boxes[box_index].remove(self.boxes[box_index][lens_index])

    def _FindLensInBox(self, box_index, label):
        for i, lens in enumerate(self.boxes[box_index]):
            if lens[0] == label:
                return i
        return -1

    def _GetLabelOperations(self):
        words = self.line.strip().split(",")
        res = []
        for word in words:
            label, op, focal_num = "", "", 0
            if word[-1] == "-":
                label, op = word[:-1], "-"
            else:
                label = word[: word.index("=")]
                op = "="
                focal_num = int(word[word.index("=") + 1 :])
            res.append((label, op, focal_num))
        return res

    def _Hash(self, s):
        curr = 0
        for c in s:
            curr += ord(c)
            curr = (17 * curr) % 256
        return curr


if __name__ == "__main__":
    hash = HashMap("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7")
    print(hash.GetBoxesFocusPower())
