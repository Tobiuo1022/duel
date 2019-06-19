import player

class Jackpot:
    money = 0

    def payJP(self, players):
        sum = 0 #全プレイヤーの表の合計.
        for p in players:
            sum += p.payRatio

        if sum == 0:
            print('お支払いはありません.')
        else:
            unit = self.money/sum #sum等分の1個分.
            for p in players:
                bonus = int(unit*p.payRatio)
                p.money += bonus
                self.money -= bonus
                if bonus == 0:
                    print(p.name +'さんへのお支払いはありません.')
                else:
                    print(p.name +'さんへ'+ str(bonus) +'円をお支払いします.')
