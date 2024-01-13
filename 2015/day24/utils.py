class Santa:
    def __init__(self, packages, num_groups):
        self.packages = packages
        self.weight = sum(self.packages) // num_groups
        self.packages.sort()
        self.all_subsets = set()
        self.ideal_subsets = set()

    def GetIdealConfigQE(self):
        self._GetAllSubsets()
        self._GetIdealSubsets()
        min_QE = float("inf")
        min_size = len(min(self.ideal_subsets, key=lambda x: len(x)))
        for ss in self.ideal_subsets:
            if len(ss) == min_size:
                min_QE = min(min_QE, self._QE(ss))
        return min_QE

    def _GetIdealSubsets(self):
        print("[*] Finding Partitions...")
        for i, ss in enumerate(self.all_subsets):
            if i % 40_000 == 0:
                percentage = "{:.2f}".format(i / len(self.all_subsets) * 100)
                print(f"{percentage}%")
            ss_prime = self._SubtractSet(ss)
            if self._IsPartitionableIn2(ss_prime):
                self.ideal_subsets.add(ss)

    def _IsPartitionableIn2(self, s):
        def _Recursion(curr_index, curr_sum):
            if curr_sum == self.weight: return True
            if curr_sum > self.weight: return False
            if curr_index == len(s): return False
            if _Recursion(curr_index+1, curr_sum+s[curr_index]):
                return True
            if _Recursion(curr_index+1, curr_sum):
                return True
            return False
        return _Recursion(0, 0)

    def _SubtractSet(self, s):
        init_set = set(self.packages.copy())
        for element in s:
            init_set.remove(element)
        return list(init_set)

    def _IsPartition(self, i, j, k):
        S = set()
        for element in i:
            S.add(element)
        for element in j:
            S.add(element)
        for element in k:
            S.add(element)
        return len(S) == len(self.packages)

    def _GetAllSubsets(self):
        print("[*] Generating all subsets...")
        self._GetAllSubsetsRecursive(0, [], 0)

    def _GetAllSubsetsRecursive(self, curr_index, curr_package_list, curr_sum):
        if curr_sum == self.weight:
            self.all_subsets.add(tuple(curr_package_list))
            return
        if curr_sum > self.weight:
            return
        if curr_index == len(self.packages):
            return
        # With      packages[curr_index]
        curr_package_list.append(self.packages[curr_index])
        self._GetAllSubsetsRecursive(
            curr_index + 1, curr_package_list, curr_sum + self.packages[curr_index])
        # Without   packages[curr_index]
        curr_package_list.pop()
        self._GetAllSubsetsRecursive(curr_index + 1, curr_package_list, curr_sum)

    def _QE(self, subset):
        i = 1
        for item in subset:
            i *= item
        return i


if __name__ == "__main__":
    santa = Santa([1, 2, 3, 4, 5, 7, 8, 9, 10, 11])
    print(santa.GetIdealConfigQE())
