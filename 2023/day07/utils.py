import functools

class Cards:
    def __init__(self, text):
        self.text = text
        self.bid_map = {}  # card => bid
        self._GetCards()
        self.cards = list(self.bid_map.keys())
        self.labels = list(reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]))

    def GetTotalWinnings(self):
        self.cards.sort(key=functools.cmp_to_key(self._CompareHand))
        self.cards.reverse()
        total = 0
        for i in range(len(self.cards)):
            total += (i+1) * self.bid_map[self.cards[i]]
        return total
    
    def GetTotalWinnings2(self):
        self.labels = list(reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]))
        self.cards.sort(key=functools.cmp_to_key(self._CompareHand2))
        self.cards.reverse()
        total = 0
        for i in range(len(self.cards)):
            total += (i+1) * self.bid_map[self.cards[i]]
        return total

    def _CompareHand(self, hand1, hand2):
        type1 = self._GetHandType(hand1)
        type2 = self._GetHandType(hand2)
        if type1 < type2:
            return 1
        if type1 > type2:
            return -1
        for i in range(5):
            i1, i2 = self.labels.index(hand1[i]), self.labels.index(hand2[i])
            if i1 < i2:
                return 1
            if i1 > i2:
                return -1
        return 0
    
    def _CompareHand2(self, hand1, hand2):
        type1 = self._GetMaxHandType(hand1)
        type2 = self._GetMaxHandType(hand2)
        if type1 < type2:
            return 1
        if type1 > type2:
            return -1
        for i in range(5):
            i1, i2 = self.labels.index(hand1[i]), self.labels.index(hand2[i])
            if i1 < i2:
                return 1
            if i1 > i2:
                return -1
        return 0

    def _GetMaxHandType(self, hand):
        max_type = 0
        for label in self.labels:
            copy_hand = hand.replace("J", label)
            max_type = max(max_type, self._GetHandType(copy_hand))
        return max_type

    def _GetHandType(self, hand):
        type_count = {}
        for c in hand:
            if type_count.get(c) == None:
                type_count[c] = 0
            type_count[c] += 1
        labels = list(type_count.keys())
        labels.sort(key=lambda x: type_count[x])
        if len(type_count) == 1:  # Five of a kind
            return 7
        if len(type_count) == 2:
            if type_count[labels[0]] == 1 and type_count[labels[1]] == 4:  # Four of a kind
                return 6
            if type_count[labels[0]] == 2 and type_count[labels[1]] == 3:  # Full house
                return 5
        if len(type_count) == 3:
            if type_count[labels[0]] == 1 and type_count[labels[1]] == 1 and type_count[labels[2]] == 3:  # Three of a kind
                return 4
            if type_count[labels[0]] == 1 and type_count[labels[1]] == 2 and type_count[labels[2]] == 2:  # Two pair
                return 3
        if len(type_count) == 4:
            if type_count[labels[0]] == 1 and type_count[labels[1]] == 1 and type_count[labels[2]] == 1 and type_count[labels[3]] == 2:  # One pair
                return 2
        if len(type_count) == 5:
            return 1
        return 0

    def _GetCards(self):
        for line in self.text:
            card, bid = line.split()[0].strip(), int(line.split()[1])
            self.bid_map[card] = bid