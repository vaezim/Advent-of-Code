class SpinLock:
    def __init__(self, step_size):
        self.step = step_size

    def CreateBuffer1(self):
        buffer = [0]
        for curr in range(1, 2017 + 1):
            i = (buffer.index(curr - 1) + self.step) % len(buffer)
            buffer.insert(i + 1, curr)
        self.buffer = buffer
        return buffer[buffer.index(len(buffer) - 1) + 1]

    def CreateBuffer2(self):
        index_one_val = 0
        curr = [0, 0]  # [val, index]
        arr_size = 1
        for _ in range(50_000_000):
            curr_index = curr[1]
            next_index = ((curr_index + self.step) % arr_size) + 1
            if next_index == 1:
                index_one_val = arr_size
            curr = [arr_size, next_index]
            arr_size += 1
        return index_one_val


if __name__ == "__main__":
    spinlock = SpinLock(3)
    print(spinlock.CreateBuffer1())
