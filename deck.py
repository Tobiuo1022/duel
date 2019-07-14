import random, player

class Deck:
    cards = []

    def shuffle(self):
        self.cards.clear()
        for n in range(60):
            self.cards.append(n)

    def deal_cards(self, player):
        for i in range(5): #手札は5枚.
            rand_num = random.randint(0, len(self.cards)-1)
            card = self.cards.pop(rand_num) #デッキの中からランダムでカードを一枚引く.
            hand = linkCard(card)
            player.hands.append(hand)

def linkCard(card):
        """
        cardの数字をモードで返す.変換器.
        """
        mode = None
        if 0 <= card and card <= 19:
            mode = 'ブラフ'
        elif 20 <= card and card <= 39:
            mode = 'カウンター'
        else:
            mode = 'トリプルアップ'
        return mode
