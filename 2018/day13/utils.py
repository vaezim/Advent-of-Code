from copy import deepcopy

class Carts:
    def __init__(self, lines):
        self.carts = []
        self.grid = lines
        self.crashes = []
        self._FindCarts()
        self._SortCarts()
        self.copy_carts = deepcopy(self.carts)
        self.destroyingCrash = False
        self.pendingDestroy = []

    def GetFirstCrash(self):
        self.destroyingCrash = False
        while len(self.crashes) == 0:
            self._Tick()
        return (self.crashes[0][1], self.crashes[0][0])
    
    def GetLastRemainingCart(self):
        self.destroyingCrash = True
        self.carts = deepcopy(self.copy_carts)
        while len(self.carts) > 1:
            self._Tick()
        return (self.carts[0][1], self.carts[0][0])

    def _Tick(self):
        self._SortCarts()
        for i in range(len(self.carts)):
            if self.carts[i] in self.pendingDestroy:
                continue
            self._MoveCart(self.carts[i])
        for c in self.pendingDestroy:
            self.carts.remove(c)
        self.pendingDestroy.clear()

    def _MoveCart(self, cart):
        i, j, direction, rem = \
            cart[0], cart[1], cart[2], cart[3]
        next_i, next_j = i, j
        # Right
        if direction == ">":
            next_j += 1
            if self.grid[next_i][next_j] == "\\":
                cart[2] = "v"
            elif self.grid[next_i][next_j] == "/":
                cart[2] = "^"
            elif self.grid[next_i][next_j] == "+":
                if rem == 0: cart[2] = "^"
                elif rem == 2: cart[2] = "v"
                cart[3] = (cart[3] + 1) % 3
        # Left
        elif direction == "<":
            next_j -= 1
            if self.grid[next_i][next_j] == "\\":
                cart[2] = "^"
            elif self.grid[next_i][next_j] == "/":
                cart[2] = "v"
            elif self.grid[next_i][next_j] == "+":
                if rem == 0: cart[2] = "v"
                elif rem == 2: cart[2] = "^"
                cart[3] = (cart[3] + 1) % 3
        # Up
        elif direction == "^":
            next_i -= 1
            if self.grid[next_i][next_j] == "\\":
                cart[2] = "<"
            elif self.grid[next_i][next_j] == "/":
                cart[2] = ">"
            elif self.grid[next_i][next_j] == "+":
                if rem == 0: cart[2] = "<"
                elif rem == 2: cart[2] = ">"
                cart[3] = (cart[3] + 1) % 3
        # Down
        elif direction == "v":
            next_i += 1
            if self.grid[next_i][next_j] == "\\":
                cart[2] = ">"
            elif self.grid[next_i][next_j] == "/":
                cart[2] = "<"
            elif self.grid[next_i][next_j] == "+":
                if rem == 0: cart[2] = ">"
                elif rem == 2: cart[2] = "<"
                cart[3] = (cart[3] + 1) % 3
        # Check crash
        otherCart = self._IsCartHere(next_i, next_j)
        if otherCart != None:
            if not self.destroyingCrash:
                self.crashes.append((next_i, next_j))
            else:
                self.pendingDestroy.append(cart)
                self.pendingDestroy.append(otherCart)
        # Update coordinates (if cart did not crash)
        else:
            cart[0] = next_i
            cart[1] = next_j

    def _IsCartHere(self, i, j):
        for c in self.carts:
            if c[0] == i and c[1] == j:
                return c
        return None

    def _FindCarts(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] in "<>^v":
                    # [i, j, direction, cross-section-remainder(0, 1, 2)]
                    self.carts.append([i, j, self.grid[i][j], 0])
                    if self.grid[i][j] in "<>":
                        self.grid[i][j] = "-"
                    else:
                        self.grid[i][j] = "|"

    def _SortCarts(self):
        self.carts.sort(key=lambda x: (x[0], x[1]))