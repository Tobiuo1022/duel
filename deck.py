import random, player

"""
0~59の計60個の数字を用意し,0~19はダウト,20~39はカウンター,40~59はトリプルアップが割り振られる.
60個の数字からランダムでプレイヤーに配る.
"""
class Deck:
    cards = []

    def shuffle(self):
        self.cards.clear()
        for n in range(60):
            self.cards.append(n)

    def deal_cards(self, player):
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
            mode = 'ダウト'
        elif 20 <= card and card <= 39:
            mode = 'カウンター'
        else:
            mode = 'トリプルアップ'
        return mode
