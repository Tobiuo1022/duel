import unittest
import main, coin, dealer, player

class testOfPlayer(unittest.TestCase):

    def setUp(self):
        pass

    def test_noneDoubt(self):
        """
        各モードにおいてコールとフォールドが正常に行われるかテストする関数.
        ダウトは無し.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        d = dealer.Dealer()
        p1 = player.Player(1, '1さん')
        p2 = player.Player(2, '2さん')
        p3 = player.Player(3, '3さん')
        p4 = player.Player(4, '4さん')
        players = [p1, p2, p3, p4]

        self.assertEqual(p1.money, 10000)
        self.assertEqual(p1.counter, 0)
        self.assertEqual(p2.money, 10000)
        self.assertEqual(p2.counter, 0)
        self.assertEqual(p1.money, 10000)
        self.assertEqual(p1.counter, 0)
        self.assertEqual(p1.money, 10000)
        self.assertEqual(p1.counter, 0)

        #モードの代入.
        p1.assign_mode(0)
        p2.assign_mode(0)
        p3.assign_mode(0)
        p4.assign_mode(0)

        #賭け金の代入.
        p1.assign_predict(0)
        p2.assign_predict(0)
        p3.assign_predict(1)
        p4.assign_predict(1)

        p1.assign_bet(100)
        p2.assign_bet(200)
        p3.assign_bet(300)
        p4.assign_bet(400)

        self.assertEqual(p1.mode, 0)
        self.assertEqual(p1.predict, 0)
        self.assertEqual(p1.bet, 100)
        self.assertEqual(p1.money, 9900)

        self.assertEqual(p2.mode, 0)
        self.assertEqual(p2.predict, 0)
        self.assertEqual(p2.bet, 200)
        self.assertEqual(p2.money, 9800)

        self.assertEqual(p3.mode, 0)
        self.assertEqual(p3.predict, 1)
        self.assertEqual(p3.bet, 300)
        self.assertEqual(p3.money, 9700)

        self.assertEqual(p4.mode, 0)
        self.assertEqual(p4.predict, 1)
        self.assertEqual(p4.bet, 400)
        self.assertEqual(p4.money, 9600)

        #コイントス
        c.num = 0

        #コールの代入.
        p1.assign_call(c.num, 0) #的中し,コールする.
        p2.assign_call(c.num, 1) #的中しているが降りる.
        p3.assign_call(c.num, 0) #外したがコールする.
        p4.assign_call(c.num, 1) #外し,降りる.

        self.assertEqual(p1.isCall, True)
        self.assertEqual(p1.bluff, 0)
        self.assertEqual(p1.predict, 0)

        self.assertEqual(p2.isCall, False)
        self.assertEqual(p2.bluff, 1)
        self.assertEqual(p2.predict, 1)

        self.assertEqual(p3.isCall, True)
        self.assertEqual(p3.bluff, 1)
        self.assertEqual(p3.predict, 0)

        self.assertEqual(p4.isCall, False)
        self.assertEqual(p4.bluff, 0)
        self.assertEqual(p4.predict, 1)

        d.pay(c, p1)
        d.pay(c, p2)
        d.pay(c, p3)
        d.pay(c, p4)

        self.assertEqual(p1.money, 10100)
        self.assertEqual(p2.money, 9800)
        self.assertEqual(p3.money, 10300)
        self.assertEqual(p4.money, 9600)

def test_betting(player, predict, bet):
    """
    引数 :
        predict : 予想する面.表は0,裏は1.
        bet : 賭ける額.
    """
    player.predict = predict
    player.bet = bet
    player.money -= player.bet

def test_callOrFold(player, coin, ans):
    """
    引数 :
        ans : 降りるなら0,降りないなら1が入る.
    """
    if player.predict == coin.num: #プレイヤーの予想とコインが一致してるかの判定
        if ans == 0: #的中しているが降りる.
            player.bluff = 1
            player.predict += player.bluff
            player.call = 0
        else: #的中し,コールする.
            player.bluff = 0
            player.call = 1
    else:
        if ans == 0: #外し,降りる.
            player.bluff = 0
            player.call = 0
        else: #外したがコールする.
            player.bluff = 1
            player.predict += player.bluff
            player.call = 1

if __name__ == '__main__':
    unittest.main()
