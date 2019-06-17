import unittest
import main, coin, dealer, player

class testOfPlayer(unittest.TestCase):

    def setUp(self):
        pass

    def test_call_bluff(self):
        """
        ブラフモードにおいてコールとフォールドが正常に行われるかテストする関数.
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
        for p in players:
            p.assign_mode(0)

        #賭け金の代入.
        p1.assign_predict(0)
        p2.assign_predict(0)
        p3.assign_predict(1)
        p4.assign_predict(1)

        for p in players:
            p.assign_bet(100)

        for p in players:
            self.assertEqual(p.mode, 0)
            self.assertEqual(p.bet, 100)
            self.assertEqual(p.money, 9900)

        self.assertEqual(p1.predict, 0)
        self.assertEqual(p2.predict, 0)
        self.assertEqual(p3.predict, 1)
        self.assertEqual(p4.predict, 1)

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

        for p in players:
            d.pay(c, p)

        for p in players:
            p.updateValue()

        self.assertEqual(p1.money, 10100)
        self.assertEqual(p1.counter, 0)
        self.assertEqual(p2.money, 9900)
        self.assertEqual(p2.counter, 50)
        self.assertEqual(p3.money, 10100)
        self.assertEqual(p3.counter, 0)
        self.assertEqual(p4.money, 9900)
        self.assertEqual(p4.counter, 50)

    def test_call_counter(self):
        """
        カウンターモードにおいてコールとフォールドが正常に行われるかテストする関数.
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
        for p in players:
            p.assign_mode(1)

        #賭け金の代入.
        p1.assign_predict(0)
        p2.assign_predict(0)
        p3.assign_predict(1)
        p4.assign_predict(1)

        for p in players:
            p.assign_bet(100)

        for p in players:
            self.assertEqual(p.mode, 1)
            self.assertEqual(p.bet, 100)
            self.assertEqual(p.money, 9900)

        self.assertEqual(p1.predict, 0)
        self.assertEqual(p2.predict, 0)
        self.assertEqual(p3.predict, 1)
        self.assertEqual(p4.predict, 1)

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

        for p in players:
            d.pay(c, p)

        for p in players:
            p.updateValue()

        self.assertEqual(p1.money, 10100)
        self.assertEqual(p1.counter, 0)
        self.assertEqual(p2.money, 9900)
        self.assertEqual(p2.counter, 50)
        self.assertEqual(p3.money, 10100)
        self.assertEqual(p3.counter, 0)
        self.assertEqual(p4.money, 9900)
        self.assertEqual(p4.counter, 50)

    def test_call_doubleUp(self):
        """
        ダブルアップモードにおいてコールとフォールドが正常に行われるかテストする関数.
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
        for p in players:
            p.assign_mode(2)

        #賭け金の代入.
        p1.assign_predict(0)
        p2.assign_predict(0)
        p3.assign_predict(1)
        p4.assign_predict(1)

        for p in players:
            p.assign_bet(100)

        for p in players:
            self.assertEqual(p.mode, 2)
            self.assertEqual(p.bet, 100)
            self.assertEqual(p.money, 9900)

        self.assertEqual(p1.predict, 0)
        self.assertEqual(p2.predict, 0)
        self.assertEqual(p3.predict, 1)
        self.assertEqual(p4.predict, 1)

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

        for p in players:
            d.pay(c, p)

        for p in players:
            p.updateValue()

        self.assertEqual(p1.money, 10100)
        self.assertEqual(p1.counter, 0)
        self.assertEqual(p2.money, 9900)
        self.assertEqual(p2.counter, 50)
        self.assertEqual(p3.money, 10300) #ダブルアップによって4倍.
        self.assertEqual(p3.counter, 0)
        self.assertEqual(p4.money, 9900)
        self.assertEqual(p4.counter, 50)

    def test_doubt_bluff(self):
        """
        ブラフモードにおいてダウトが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        d = dealer.Dealer()
        p1 = player.Player(1, '1さん') #奇数組はダウト係.
        p2 = player.Player(2, '2さん') #ブラフ,的中,コール.
        p3 = player.Player(3, '3さん')
        p4 = player.Player(4, '4さん') #ブラフ,的中,フォールド.
        p5 = player.Player(5, '5さん')
        p6 = player.Player(6, '6さん') #ブラフ,外れ,コール.
        p7 = player.Player(7, '7さん')
        p8 = player.Player(8, '8さん') #ブラフ,外れ,フォールド.
        p9 = player.Player(9, '9さん')
        p10 = player.Player(10, '10さん') #カウンター,的中,コール.
        p11 = player.Player(11, '11さん')
        p12 = player.Player(12, '12さん') #カウンター,的中,フォールド.
        p13 = player.Player(13, '13さん')
        p14 = player.Player(14, '14さん') #カウンター,外れ,コール.
        p15 = player.Player(15, '15さん')
        p16 = player.Player(16, '16さん') #カウンター,外れ,フォールド.
        p17 = player.Player(17, '17さん')
        p18 = player.Player(18, '18さん') #ダブルアップ,的中,コール.
        p19 = player.Player(19, '19さん')
        p20 = player.Player(20, '20さん') #ダブルアップ,的中,フォールド.
        p21 = player.Player(21, '21さん')
        p22 = player.Player(22, '22さん') #ダブルアップ,外れ,コール.
        p23 = player.Player(23, '23さん')
        p24 = player.Player(24, '24さん') #ダブルアップ,外れ,フォールド.
        players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24]

        #モードの代入.
        n = 0
        for p in players:
            n += 1
            if n%2 == 1: #奇数組はブラフモード.
                p.assign_mode(0)
            elif n <= 8: #ブラフモード.
                p.assign_mode(0)
            elif n <= 16: #カウンターモード.
                p.assign_mode(1)
            elif n <= 24: #ダブルアップモード.
                p.assign_mode(2)

        #賭け金の代入.
        n = 0
        for p in players:
            n += 1
            m = n%8
            if m == 6 or m == 0:
                p.assign_predict(1) #外れ
            else:
                p.assign_predict(0) #的中

        for p in players:
            p.assign_bet(100)

        #コイントス
        c.num = 0

        #コールの代入.
        n = 0
        for p in players:
            n += 1
            if n%4 == 0:
                p.assign_call(c.num, 1)
            else:
                p.assign_call(c.num, 0)

        #ダウトの入力.
        n = 0
        for p in players:
            n += 1
            if n%2 == 1: #ダウト係は次のプレイヤーをダウトする.
                p.assign_doubt(n+1)
            else:
                p.assign_doubt(0) #ダウトされる側はダウトしない.

        #detect
        n = 0
        for p in players:
            n += 1
            if n%2 == 1:
                p.detect(players)

        for p in players:
            d.pay(c, p)

        for p in players:
            p.updateValue()

        self.assertEqual(p1.money, 10050)
        self.assertEqual(p2.money, 10100)
        self.assertEqual(p3.money, 10200)
        self.assertEqual(p4.money, 10050)
        self.assertEqual(p5.money, 10200)
        self.assertEqual(p6.money, 9850)
        self.assertEqual(p7.money, 10050)
        self.assertEqual(p8.money, 9900)
        self.assertEqual(p9.money, 10050)
        self.assertEqual(p10.money, 10100)
        self.assertEqual(p11.money, 10200)
        self.assertEqual(p12.money, 10000)
        self.assertEqual(p13.money, 10200)
        self.assertEqual(p14.money, 9800)
        self.assertEqual(p15.money, 10050)
        self.assertEqual(p16.money, 9900)
        self.assertEqual(p17.money, 10050)
        self.assertEqual(p18.money, 10100)
        self.assertEqual(p19.money, 10300)
        self.assertEqual(p20.money, 9900)
        self.assertEqual(p21.money, 10300)
        self.assertEqual(p22.money, 9700)
        self.assertEqual(p23.money, 10050)
        self.assertEqual(p24.money, 9900)

        n = 0
        for p in players:
            n += 1
            if n%4 == 0:
                self.assertEqual(p.counter, 50)
            else:
                self.assertEqual(p.counter, 0)

    def test_doubt_counter(self):
        """
        カウンターモードにおいてダウトが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        d = dealer.Dealer()
        p1 = player.Player(1, '1さん') #奇数組はダウト係.
        p2 = player.Player(2, '2さん') #ブラフ,的中,コール.
        p3 = player.Player(3, '3さん')
        p4 = player.Player(4, '4さん') #ブラフ,的中,フォールド.
        p5 = player.Player(5, '5さん')
        p6 = player.Player(6, '6さん') #ブラフ,外れ,コール.
        p7 = player.Player(7, '7さん')
        p8 = player.Player(8, '8さん') #ブラフ,外れ,フォールド.
        p9 = player.Player(9, '9さん')
        p10 = player.Player(10, '10さん') #カウンター,的中,コール.
        p11 = player.Player(11, '11さん')
        p12 = player.Player(12, '12さん') #カウンター,的中,フォールド.
        p13 = player.Player(13, '13さん')
        p14 = player.Player(14, '14さん') #カウンター,外れ,コール.
        p15 = player.Player(15, '15さん')
        p16 = player.Player(16, '16さん') #カウンター,外れ,フォールド.
        p17 = player.Player(17, '17さん')
        p18 = player.Player(18, '18さん') #ダブルアップ,的中,コール.
        p19 = player.Player(19, '19さん')
        p20 = player.Player(20, '20さん') #ダブルアップ,的中,フォールド.
        p21 = player.Player(21, '21さん')
        p22 = player.Player(22, '22さん') #ダブルアップ,外れ,コール.
        p23 = player.Player(23, '23さん')
        p24 = player.Player(24, '24さん') #ダブルアップ,外れ,フォールド.
        players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24]

        #モードの代入.
        n = 0
        for p in players:
            n += 1
            if n%2 == 1: #奇数組はカウンターモード.
                p.assign_mode(1)
            elif n <= 8: #ブラフモード.
                p.assign_mode(0)
            elif n <= 16: #カウンターモード.
                p.assign_mode(1)
            elif n <= 24: #ダブルアップモード.
                p.assign_mode(2)

        #賭け金の代入.
        n = 0
        for p in players:
            n += 1
            m = n%8
            if m == 6 or m == 0:
                p.assign_predict(1) #外れ
            else:
                p.assign_predict(0) #的中

        for p in players:
            p.assign_bet(100)

        #コイントス
        c.num = 0

        #コールの代入.
        n = 0
        for p in players:
            n += 1
            if n%4 == 0:
                p.assign_call(c.num, 1)
            else:
                p.assign_call(c.num, 0)

        #ダウトの入力.
        n = 0
        for p in players:
            n += 1
            if n%2 == 1: #ダウト係は次のプレイヤーをダウトする.
                p.assign_doubt(n+1)
            else:
                p.assign_doubt(0) #ダウトされる側はダウトしない.

        #detect
        n = 0
        for p in players:
            n += 1
            if n%2 == 1:
                p.detect(players)

        for p in players:
            d.pay(c, p)

        for p in players:
            p.updateValue()

        self.assertEqual(p1.money, 10000)
        self.assertEqual(p2.money, 10100)
        self.assertEqual(p3.money, 10200)
        self.assertEqual(p4.money, 10050)
        self.assertEqual(p5.money, 10200)
        self.assertEqual(p6.money, 9850)
        self.assertEqual(p7.money, 10000)
        self.assertEqual(p8.money, 9900)
        self.assertEqual(p9.money, 10000)
        self.assertEqual(p10.money, 10100)
        self.assertEqual(p11.money, 10200)
        self.assertEqual(p12.money, 10000)
        self.assertEqual(p13.money, 10200)
        self.assertEqual(p14.money, 9800)
        self.assertEqual(p15.money, 10000)
        self.assertEqual(p16.money, 9900)
        self.assertEqual(p17.money, 10000)
        self.assertEqual(p18.money, 10100)
        self.assertEqual(p19.money, 10200)
        self.assertEqual(p20.money, 10000)
        self.assertEqual(p21.money, 10200)
        self.assertEqual(p22.money, 9800)
        self.assertEqual(p23.money, 10000)
        self.assertEqual(p24.money, 9900)

        n = 0
        for p in players:
            n += 1
            if n%4 == 0:
                self.assertEqual(p.counter, 50)
            else:
                self.assertEqual(p.counter, 0)

    def test_doubt_doubleUp(self):
        """
        ダブルアップモードにおいてダウトが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        d = dealer.Dealer()
        p1 = player.Player(1, '1さん') #奇数組はダウト係.
        p2 = player.Player(2, '2さん') #ブラフ,的中,コール.
        p3 = player.Player(3, '3さん')
        p4 = player.Player(4, '4さん') #ブラフ,的中,フォールド.
        p5 = player.Player(5, '5さん')
        p6 = player.Player(6, '6さん') #ブラフ,外れ,コール.
        p7 = player.Player(7, '7さん')
        p8 = player.Player(8, '8さん') #ブラフ,外れ,フォールド.
        p9 = player.Player(9, '9さん')
        p10 = player.Player(10, '10さん') #カウンター,的中,コール.
        p11 = player.Player(11, '11さん')
        p12 = player.Player(12, '12さん') #カウンター,的中,フォールド.
        p13 = player.Player(13, '13さん')
        p14 = player.Player(14, '14さん') #カウンター,外れ,コール.
        p15 = player.Player(15, '15さん')
        p16 = player.Player(16, '16さん') #カウンター,外れ,フォールド.
        p17 = player.Player(17, '17さん')
        p18 = player.Player(18, '18さん') #ダブルアップ,的中,コール.
        p19 = player.Player(19, '19さん')
        p20 = player.Player(20, '20さん') #ダブルアップ,的中,フォールド.
        p21 = player.Player(21, '21さん')
        p22 = player.Player(22, '22さん') #ダブルアップ,外れ,コール.
        p23 = player.Player(23, '23さん')
        p24 = player.Player(24, '24さん') #ダブルアップ,外れ,フォールド.
        players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24]

        #モードの代入.
        n = 0
        for p in players:
            n += 1
            if n%2 == 1: #奇数組はダブルアップモード.
                p.assign_mode(2)
            elif n <= 8: #ブラフモード.
                p.assign_mode(0)
            elif n <= 16: #カウンターモード.
                p.assign_mode(1)
            elif n <= 24: #ダブルアップモード.
                p.assign_mode(2)

        #賭け金の代入.
        n = 0
        for p in players:
            n += 1
            m = n%8
            if m == 6 or m == 0:
                p.assign_predict(1) #外れ
            else:
                p.assign_predict(0) #的中

        for p in players:
            p.assign_bet(100)

        #コイントス
        c.num = 0

        #コールの代入.
        n = 0
        for p in players:
            n += 1
            if n%4 == 0:
                p.assign_call(c.num, 1)
            else:
                p.assign_call(c.num, 0)

        #ダウトの入力.
        n = 0
        for p in players:
            n += 1
            if n%2 == 1: #ダウト係は次のプレイヤーをダウトする.
                p.assign_doubt(n+1)
            else:
                p.assign_doubt(0) #ダウトされる側はダウトしない.

        #detect
        n = 0
        for p in players:
            n += 1
            if n%2 == 1:
                p.detect(players)

        for p in players:
            d.pay(c, p)

        for p in players:
            p.updateValue()

        self.assertEqual(p1.money, 10000)
        self.assertEqual(p2.money, 10100)
        self.assertEqual(p3.money, 10200)
        self.assertEqual(p4.money, 10050)
        self.assertEqual(p5.money, 10200)
        self.assertEqual(p6.money, 9850)
        self.assertEqual(p7.money, 10000)
        self.assertEqual(p8.money, 9900)
        self.assertEqual(p9.money, 10000)
        self.assertEqual(p10.money, 10100)
        self.assertEqual(p11.money, 10200)
        self.assertEqual(p12.money, 10000)
        self.assertEqual(p13.money, 10200)
        self.assertEqual(p14.money, 9800)
        self.assertEqual(p15.money, 10000)
        self.assertEqual(p16.money, 9900)
        self.assertEqual(p17.money, 10000)
        self.assertEqual(p18.money, 10100)
        self.assertEqual(p19.money, 10200)
        self.assertEqual(p20.money, 10000)
        self.assertEqual(p21.money, 10200)
        self.assertEqual(p22.money, 9800)
        self.assertEqual(p23.money, 10000)
        self.assertEqual(p24.money, 9900)

        n = 0
        for p in players:
            n += 1
            if n%4 == 0:
                self.assertEqual(p.counter, 50)
            else:
                self.assertEqual(p.counter, 0)

    def test_overlap_doubt(self):
        """
        複数のプレイヤーでダウトが重複した場合にダウトが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        d = dealer.Dealer()
        p1 = player.Player(1, '1さん')
        p2 = player.Player(2, '2さん')
        p3 = player.Player(3, '3さん')
        p4 = player.Player(4, '4さん')
        players = [p1, p2, p3, p4]

        #モードの代入.
        for p in players:
            p.assign_mode(0)

        #賭け金の代入.
        p1.assign_predict(0)
        p2.assign_predict(0)
        p3.assign_predict(1)
        p4.assign_predict(1)

        n = 0
        for p in players:
            n += 1
            p.assign_bet(100 * n)

        #コイントス
        c.num = 0

        #コールの代入.
        p1.assign_call(c.num, 0) #的中し,コールする.
        p2.assign_call(c.num, 1) #的中しているが降りる.
        p3.assign_call(c.num, 0) #外したがコールする.
        p4.assign_call(c.num, 1) #外し,降りる.

        #ダウトの入力.
        p1.assign_doubt(3)
        p2.assign_doubt(3)
        p3.assign_doubt(0)
        p4.assign_doubt(3)

        d.delete_overlap_doubt(players)

        #detect
        for p in players:
            if main.linkId(p.doubt, players) != None:
                p.detect(players)

        for p in players:
            d.pay(c, p)

        for p in players:
            p.updateValue()

        self.assertEqual(p1.money, 10100)
        self.assertEqual(p2.money, 9800)
        self.assertEqual(p3.money, 9550)
        self.assertEqual(p4.money, 9900)

if __name__ == '__main__':
    unittest.main()
