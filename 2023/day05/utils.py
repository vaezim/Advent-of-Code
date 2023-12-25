class Gardener:
    def __init__(self, text):
        self.text = text
        self.seeds = self._GetSeeds()
        self.maps = self._GetMaps()

    def GetMinSeedLocations(self):
        min_loc = float("inf")
        for seed in self.seeds:
            loc = self._GetSeedLocation(seed)
            min_loc = min(min_loc, loc)
        return min_loc
    
    def GetMinSeedRangeLocations(self):
        pass

    def _GetMinSeedRangeLocation(self, start, end):
        

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