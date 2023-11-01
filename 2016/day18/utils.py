class TrapFinder:
    def __init__(self, first_row):
        self.rows = [first_row]

    def GenerateRows(self, num):
        while (len(self.rows) < num):
            self._GenerateRow()
        return self._GetSafeNum()
    
    def _GetSafeNum(self):
        safe_num = 0
        for row in self.rows:
            for c in row:
                safe_num += c == "."
        return safe_num

    def _GenerateRow(self):
        row = ""
        last_row = "." + self.rows[-1] + "."
        for i in range(1,len(last_row)-1):
            left, center, right = last_row[i-1], last_row[i], last_row[i+1]
            if (left == "^" and center == "^" and right == ".") or \
               (right == "^" and center == "^" and left == ".") or \
               (left == "^" and center == "." and right == ".") or \
               (right == "^" and center == "." and left == "."):
                row += "^"
            else:
                row += "."
        self.rows.append(row)
        return row


if __name__ == "__main__":
    tf = TrapFinder(first_row=".^^.^.^^^^")
    print(tf.GenerateRows(10))
    