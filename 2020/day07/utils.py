import re

class Bags:
    def __init__(self, text):
        self.bags = self._Process(list(map(lambda x: x.strip(), text)))
        self.bag_nums_within_bags = {}  # bag_name => num bags within it

    def GetNumBagsWithinShinyGold(self):
        return self._GetNumBagsWithinBag("shinygold")

    def _GetNumBagsWithinBag(self, bag):
        if self.bag_nums_within_bags.get(bag) != None:
            return self.bag_nums_within_bags[bag]
        num = 0
        for b in self.bags[bag]:
            num += (int(b[1]) * (self._GetNumBagsWithinBag(b[0]) + 1))
        self.bag_nums_within_bags[bag] = num
        return num

    def GetNumBagsContainingShinyGold(self):
        containing = set()
        for bag in self.bags:
            if bag in containing:
                continue
            if self._ContainsShinyGold(bag):
                containing.add(bag)
        return len(containing)

    def _ContainsShinyGold(self, bag):
        bag_list = self.bags[bag]
        for b in bag_list:
            if b[0] == "shinygold":
                return True
        for b in bag_list:
            if self._ContainsShinyGold(b[0]):
                return True
        return False

    def _Process(self, text):
        bags = {}
        for line in text:
            bag_names = re.findall(r"\w+ \w+ bags?", line)
            bag_names = list(map(lambda x: (x.split()[0]+x.split()[1]), bag_names))
            nums = re.findall(r"\d+", line)
            bags[bag_names[0]] = []
            if not len(nums):
                continue
            for i in range(1, len(bag_names)):
                bags[bag_names[0]].append((bag_names[i],nums[i-1]))
        return bags