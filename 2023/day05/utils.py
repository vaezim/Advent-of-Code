from Ranger import Ranger

class Gardener:
    def __init__(self, text):
        self.text = text
        self.seeds = self._GetSeeds()
        self.maps = self._GetMaps()

    def GetMinSeedLocations(self):
        min_loc = float("inf")
        for seed in self.seeds:
            min_loc = min(min_loc, self._GetSeedLocation(seed))
        return min_loc
    
    def GetMinSeedRangeLocations(self):
        min_loc = float("inf")
        for i in range(0, len(self.seeds), 2):
            seed_range = [self.seeds[i], self.seeds[i]+self.seeds[i+1]]
            locs = self._GetSeedRangeLocations(seed_range)
            min_loc = min(min_loc, locs[0][0])
        return min_loc

    def _GetSeedRangeLocations(self, seed_range):
        ranges = [seed_range]
        for i, map in enumerate(self.maps):
            output = []
            for r in ranges:
                R = Ranger(r[0], r[1])
                transforms = self._CreateTransformFromMap(map)
                layerOutput = R.Transform(transforms)
                output.extend(layerOutput)
            ranges = R.MergeRanges(output)
        return ranges

    def _CreateTransformFromMap(self, m):
        transforms = {}
        for item in m:
            transforms[(item[1], item[1]+item[2]-1)] = item[0] - item[1]
        return transforms

    def _GetSeedLocation(self, seed) -> int:
        for mapping in self.maps:
            seed = self._GetMappedValue(seed=seed, mapping=mapping)
        return seed

    def _GetMappedValue(self, seed, mapping) -> int:
        for map in mapping:
            dst, src, rng = map
            if src <= seed < (src + rng):
                return seed + (dst - src)
        return seed

    def _GetSeeds(self) -> list:
        seed_line = self.text[0].strip()
        seeds = seed_line[seed_line.index(':')+1:].strip().split()
        seeds = list(map(lambda x: int(x), seeds))
        return seeds
    
    def _GetMaps(self) -> list:
        maps = []  # list of mapping layers
        mapping = []
        for line in self.text:
            if not line[0].isdigit():
                if len(mapping) > 0:
                    maps.append(mapping.copy())
                    mapping.clear()
                continue
            mapping.append(tuple(map(lambda x: int(x), line.strip().split())))
        if len(mapping) > 0:
            maps.append(mapping.copy())
        return maps