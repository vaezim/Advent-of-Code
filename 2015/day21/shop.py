
class Shop:
    def __init__(self):
        self.weapons = {  # "weapon_name": (Cost, Damage, Armor)
            "Dagger":       (8,  4, 0),
            "Shortsword":   (10, 5, 0),
            "Warhammer":    (25, 6, 0),
            "Longsword":    (40, 7, 0),
            "Greataxe":     (74, 8, 0)
        }
        self.armors = {  # "armor_name": (Cost, Damage, Armor)
            "Leather":      (13, 0, 1),
            "Chainmail":    (31, 0, 2),
            "Splintmail":   (53, 0, 3),
            "Bandedmail":   (75, 0, 4),
            "Platemail":    (102, 0, 5),
            "NaN":          (0, 0, 0)
        }
        self.rings = {  # "ring_name": (Cost, Damage, Armor)
            "Damage+1":     (25, 1, 0),
            "Damage+2":     (50, 2, 0),
            "Damage+3":     (100, 3, 0),
            "Defense+1":    (20, 0, 1),
            "Defense+2":    (40, 0, 2),
            "Defense+3":    (80, 0, 3),
            "NaN":          (0, 0, 0)
        }
    