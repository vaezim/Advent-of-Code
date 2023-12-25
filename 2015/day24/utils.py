
class Santa:
    def __init__(self, packages):
        self.packages = packages
        self.weight = sum(self.packages) // 3
        self.packages.sort()

        self.curr_subset = []
        self.weightSubsets = set()

    def GetIdealConfigQE(self):
        partitions = self._GetPartitions()
        minPartitionLen = float("inf")
        minQE = float("inf")
        for part in partitions:
            minPart = min(part, key=lambda x: len(x))
            if len(minPart) <= minPartitionLen:
                minPartitionLen = len(minPart)
                minQE = min(minQE, self._Product(minPart))
        return minQE

    def _GetPartitions(self):
        partitions = set()
        if len(self.weightSubsets) == 0:
            print("[*] Generating Candidate Subsets for Partitions...")
            self._GeneratePartitionCandidates()
        self.weightSubsets = list(self.weightSubsets)
        minPartitionLen = float("inf")
        print("[*] Generating Partitions...")
        for i in range(len(self.weightSubsets)):
            for j in range(1,len(self.weightSubsets)):
                for k in range(2,len(self.weightSubsets)):
                    currMinPartitionLen = min(len(self.weightSubsets[i]),len(self.weightSubsets[j]),len(self.weightSubsets[k]))
                    if currMinPartitionLen <= minPartitionLen:
                        if self._IsPartition(self.weightSubsets[i],self.weightSubsets[j],self.weightSubsets[k]):
                            partitions.add((self.weightSubsets[i],self.weightSubsets[j],self.weightSubsets[k]))
                            minPartitionLen = currMinPartitionLen
        return partitions

    def _GeneratePartitionCandidates(self, last=0):
        S = sum(self.curr_subset)
        if S == self.weight:
            self.weightSubsets.add(tuple(sorted(self.curr_subset)))
            return
        if S > self.weight:
            return -1
        if last >= len(self.packages): return
        for i in range(last,len(self.packages)):
            # Don't add packages[last]
            self._GeneratePartitionCandidates(i+1)
            # Add packages[last]
            self.curr_subset.append(self.packages[i])
            ret = self._GeneratePartitionCandidates(i+1)
            self.curr_subset.pop()
            if ret == -1: return # don't check larger numbers

    def _IsPartition(self, subset1, subset2, subset3):
        S = set()
        for i in subset1:
            S.add(i)
        for i in subset2:
            S.add(i)
        for i in subset3:
            S.add(i)
        return len(S) == len(self.packages)

    def _Product(self, nums):
        p = 1
        for i in nums:
            p *= i
        return p


if __name__ == "__main__":
    # packages = [1,2,3]
    packages = [1,2,3,4,5,7,8,9,10,11]
    santa = Santa(packages)
    print(santa.GetIdealConfigQE())
