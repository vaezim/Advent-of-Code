class ElfRecipe:
    def __init__(self, N):
        self.N = N
        self.recipes = [3, 7]

    def GetLast10RecipeScores(self):
        e1, e2 = 0, 1
        while len(self.recipes) < self.N + 10:
            new_recipe = self.recipes[e1] + self.recipes[e2]
            for c in str(new_recipe):
                self.recipes.append(int(c))
            e1 = (1 + e1 + self.recipes[e1]) % len(self.recipes)
            e2 = (1 + e2 + self.recipes[e2]) % len(self.recipes)
        result = ''.join(list(map(lambda x: str(x), self.recipes[-10:])))
        return result
    
    def GetWindow(self, start_index):
        target = str(self.N)
        len_target = len(target)
        len_list = len(self.recipes)
        if start_index < len_target:
            return -1
        for i in range(start_index, len_list):
            s = ''.join(list(map(lambda x: str(x), self.recipes[i-len_target:i])))
            if s == target:
                return i-len_target
        return -1

    def GetNumRecipesToTheLeftOfN(self):
        self.recipes = [3, 7]
        e1, e2 = 0, 1
        while True:
            old_len_recipes = len(self.recipes)
            new_recipe = self.recipes[e1] + self.recipes[e2]
            for c in str(new_recipe):
                self.recipes.append(int(c))
            e1 = (1 + e1 + self.recipes[e1]) % len(self.recipes)
            e2 = (1 + e2 + self.recipes[e2]) % len(self.recipes)
            win_idx = self.GetWindow(old_len_recipes-1)
            if win_idx > 0:
                return win_idx