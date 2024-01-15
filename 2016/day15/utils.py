class Capsule:
    def __init__(self, text):
        self.disks = self._GetDisks(text)

    def GetDisksAllignedTime(self):
        t = 0
        while True:
            all_alligned_at_pos0 = True
            for disk_index, disk in enumerate(self.disks):
                pos = self._GetDiskPosition(t, disk[0], disk[1], disk_index + 1)
                if pos != 0:
                    all_alligned_at_pos0 = False
                    break
            if all_alligned_at_pos0:
                return t
            t += 1

    def _GetDisks(self, text):
        disks = []  # (num_positions, initial_pos)
        for line in text:
            tokens = line.strip().split()
            disks.append((int(tokens[3]), int(tokens[-1][:-1])))
        return disks

    def _GetDiskPosition(self, t, period, initial_pos, disk_index):
        return (t + disk_index + initial_pos) % period
