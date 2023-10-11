from shop import Shop
from math import ceil

class RPG:
    def __init__(self):
        self.shop = Shop()
        self.player = None  # [hit_points, damage, defense]
        self.enemy = None   # [hit_points, damage, defense]

    def BuyItems(self, weapon_name, armor_name, ring1_name, ring2_name):
        cost = 0
        player = [100, 0, 0] # [hit_points, damage, defense]

        ### Weapon ###
        if self.shop.weapons.get(weapon_name) == None:
            print(f"[-] Weapon {weapon_name} does not exist!")
            return
        weapon = self.shop.weapons.get(weapon_name)
        cost += weapon[0]
        player[1] = weapon[1]
        
        ### Armor ###
        if armor_name != None:
            if self.shop.armors.get(armor_name) == None:
                print(f"[-] Armor {armor_name} does not exist!")
                return
            armor = self.shop.armors.get(armor_name)
            cost += armor[0]
            player[2] = armor[2]
        
        ### Ring 1 ###
        if ring1_name != None:
            if self.shop.rings.get(ring1_name) == None:
                print(f"[-] Ring {ring1_name} does not exist!")
                return
            ring = self.shop.rings.get(ring1_name)
            cost += ring[0]
            if "Damage" in ring1_name:
                player[1] += ring[1]
            else:
                player[2] += ring[2]

        ### Ring 2 ###
        if ring2_name != None:
            if self.shop.rings.get(ring2_name) == None:
                print(f"[-] Ring {ring2_name} does not exist!")
                return
            ring = self.shop.rings.get(ring2_name)
            cost += ring[0]
            if "Damage" in ring2_name:
                player[1] += ring[1]
            else:
                player[2] += ring[2]
        
        self._AddPlayerStats(player)
        return cost

    def AddEnemyStats(self, enemy_stats):
        self.enemy = enemy_stats

    def IsWinning(self):
        if self.player == None or self.enemy == None:
            print("[-] Player or Enemy are None.")
            return False
        player_hits = max(1, self.player[1]-self.enemy[2])
        enemy_hits = max(1, self.enemy[1]-self.player[2])
        return ceil(self.enemy[0] / player_hits) <= ceil(self.player[0] / enemy_hits)

    def GetMinGoldCost(self):
        minCost = float("inf")
        for comb in self._GetAllShopCombs():
            cost = self.BuyItems(comb[0], comb[1], comb[2], comb[3])
            if self.IsWinning():
                minCost = min(cost, minCost)
        return minCost

    def GetMaxGoldCost(self):
        maxCost = 0
        for comb in self._GetAllShopCombs():
            cost = self.BuyItems(comb[0], comb[1], comb[2], comb[3])
            if not self.IsWinning():
                maxCost = max(cost, maxCost)
        return maxCost

    def _AddPlayerStats(self, player_stats):
        self.player = player_stats

    def _GetAllShopCombs(self):
        for weapon_name in self.shop.weapons.keys():
            for armor_name in self.shop.armors.keys():
                for i, ring1_name in enumerate(self.shop.rings.keys()):
                    for j, ring2_name in enumerate(self.shop.rings.keys()):
                        if ring1_name != "NaN" and i == j:
                            continue
                        comb = [weapon_name, armor_name, ring1_name, ring2_name]
                        yield comb


if __name__ == "__main__":
    rpg = RPG()
    # rpg.BuyItems("Longsword", "Platemail", "Defense+3", None)
    # rpg.AddEnemyStats([100, 8, 9])
    rpg._AddPlayerStats([8, 5, 5])
    rpg.AddEnemyStats([12, 7, 2])
    print(f"[*] Player: {rpg.player}")
    print(f"[*] Enemy:  {rpg.enemy}")
    if rpg.IsWinning():
        print("[+] Wins :)")
    else:
        print("[-] Loses :(")
    for comb in rpg._GetAllShopCombs():
        print(comb)
        input(">> ")
    