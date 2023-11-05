class StreamParser:
    def __init__(self, text):
        self.text = text
        self.num_garbage = 0

    def GetGroupScore(self):
        clean_text = self._RemoveGarbages()
        score = 0
        stack = []
        for c in clean_text:
            if c == '{':
                stack.append(c)
            elif c == '}':
                score += len(stack)
                stack.pop()
            else:
                print(f"Invalid char in clean text: {c}")
                return -1
        return score
    
    def GetNumGarbage(self):
        return self.num_garbage

    def _RemoveGarbages(self):
        clean_text = ""
        SKIP_CHAR = False
        INSIDE_GARBAGE = False
        for c in self.text:
            if SKIP_CHAR:
                SKIP_CHAR = False
                continue
            if c == '!':
                SKIP_CHAR = True
                continue
            if INSIDE_GARBAGE:
                self.num_garbage += 1
                if c == '>':
                    INSIDE_GARBAGE = False
                    self.num_garbage -= 1
                continue
            if c == '<':
                INSIDE_GARBAGE = True
                continue
            if c == ',':
                continue
            clean_text += c
        return clean_text


if __name__ == "__main__":
    sp = StreamParser(r"{{<!!>},{<!!>},{<!!>},{<!!>}}")
    print(sp._RemoveGarbages())
    print(sp.GetGroupScore())