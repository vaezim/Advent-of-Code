from utils import ElfRecipe

# input
N = 846021

##### Part 1 #####
er = ElfRecipe(N)
result = er.GetLast10RecipeScores()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = er.GetNumRecipesToTheLeftOfN()
print(f"[+] Answer of part 2: {result}")