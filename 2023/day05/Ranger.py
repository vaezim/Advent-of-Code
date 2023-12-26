class Ranger:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.transforms = {}

    def Transform(self, transforms: map):  # (a, b) => -+shift
        self.transforms = transforms
        keys = list(transforms.keys())
        keys.sort(key=lambda x: x[0])

        ranges = []
        start = self.start

        # Find the transformations within [self.start,self.end]
        first = 0
        while keys[first][1] < self.start:
            first += 1
            if first == len(keys):
                return [[self.start,self.end]]
        last = len(keys)-1
        while keys[last][0] > self.end:
            last -= 1
            if last == -1:
                return [[self.start,self.end]]
        if first > last:
            return [[self.start,self.end]] 

        # Go through all transformations
        for T in keys[first:last+1]:
            a, b, shift = T[0], T[1], transforms[T]
            if start < a:
                ranges.append((start, a-1))
                start = a
            ranges.append((start+shift, min(b, self.end)+shift))
            start = min(b, self.end)+1
            if start > self.end:
                return self.MergeRanges(ranges)

        # Intervals after the last transformation
        Tlast = keys[-1]
        if self.end > Tlast[1]:
            ranges.append((Tlast[1]+1, self.end))
        return self.MergeRanges(ranges)

    def MergeRanges(self, ranges: list):
        if not len(ranges):
            return []
        ranges.sort(key=lambda x: x[0])
        merged_ranges = [list(ranges[0])]
        if len(ranges) == 1:
            return merged_ranges
        for r in ranges[1:]:
            if merged_ranges[-1][1] >= r[0]-1:
                merged_ranges[-1][1] = max(merged_ranges[-1][1], r[1])
            else:
                merged_ranges.append(list(r))
        return merged_ranges

if __name__ == "__main__":
    r = Ranger(220, 240)
    transforms = {
        (10, 20) :  5,
        (40, 70) : -200,
        (100,200) : 1000,
        (250,350) : -500,
        (400,600) : 2000
    }
    ranges = r.Transform(transforms)
    print(ranges)