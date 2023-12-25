class Card:
    def __init__(self, text: list):
        self.cards = self._ParseCards(text)  # [[winning_nums, nums], ...]

    def GetTotalWorth(self):
        total_worth = 0
        for card in self.cards:
            worth = 0
            for n in card[1]:
                worth += (n in card[0])
            if worth > 0:
                total_worth += 2 ** (worth-1)
        return total_worth
    
    def GetCardNum(self):
        card_num = [1] * len(self.cards)
        for i, card in enumerate(self.cards):
            worth = 0
            for n in card[1]:
                worth += (n in card[0])
            for j in range(worth):
                if i+j+1 >= len(card_num):
                    break
                card_num[i+j+1] += card_num[i]
        return sum(card_num)

    def _ParseCards(self, text: list):
        cards = []
        for line in text:
            winning_nums = line[line.index(':')+1:line.index('|')].strip().split()
            winning_nums = set(map(lambda x: int(x.strip()), winning_nums))
            nums = line[line.index('|')+1:].strip().split()
            nums = set(map(lambda x: int(x.strip()), nums))
            cards.append([winning_nums, nums])
        return cards