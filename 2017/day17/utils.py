class SpinLock:
    def __init__(self, step_size):
        self.step = step_size

    def CreateBuffer1(self):
        buffer = [0]
        for curr in range(1,2017+1):
            i = (buffer.index(curr-1) + self.step) % len(buffer)
            buffer.insert(i+1, curr)
        self.buffer = buffer
        return buffer[buffer.index(len(buffer)-1)+1]
    
    def CreateBuffer2(self):
        pass


if __name__ == "__main__":
    spinlock = SpinLock(3)
    print(spinlock.CreateBuffer1())