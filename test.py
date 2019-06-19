import unittest
import main, coin, jackpot, dealer, player

class testOfPlayer(unittest.TestCase):

    def setUp(self):
        pass

    def test_call_bluff(self):
        """
        ブラフモードにおいてコールとフォールドが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        jp = jackpot.Jackpot()
        d = dealer.Dealer()
        p1 = player.Player(1, '1さん')
        p2 = player.Player(2, '2さん')
        p3 = player.Player(3, '3さん')
        p4 = player.Player(4, '4さん')
        players = [p1, p2, p3, p4]

        self.assertEqual(jp.money, 0)

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
            d.pay(c, jp, p)

        for p in players:
            p.updateValue()

        self.assertEqual(p1.money, 10100)
        self.assertEqual(p1.counter, 0)
        self.assertEqual(p2.money, 9900)
        self.assertEqual(p2.counter, 100)
        self.assertEqual(p3.money, 10100)
        self.assertEqual(p3.counter, 0)
        self.assertEqual(p4.money, 9900)
        self.assertEqual(p4.counter, 100)

        self.assertEqual(jp.money, 200)

    def test_call_counter(self):
        """
        カウンターモードにおいてコールとフォールドが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        jp = jackpot.Jackpot()
        d = dealer.Dealer()
        p1 = player.Player(1, '1さん')
        p2 = player.Player(2, '2さん')
        p3 = player.Player(3, '3さん')
        p4 = player.Player(4, '4さん')
        players = [p1, p2, p3, p4]

        self.assertEqual(jp.money, 0)

        self.assertEqual(p1.money, 10000)
        self.assertEqual(p1.counter, 0)
        self.assertEqual(p2.money, 10000)
        self.assertEqual(p2.counter, 0)
        self.assertEqual(p1.money, 10000)
        self.assertEqual(p1.counter, 0)
        self.assertEqual(p1.money, 10000)
        self.assertEqual(p1.counter, 0)

        for p in players:
            p.counter = 300

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
            d.pay(c, jp, p)

        for p in players:
            p.updateValue()

        self.assertEqual(p1.money, 10100)
        self.assertEqual(p1.counter, 225)
        self.assertEqual(p2.money, 9900)
        self.assertEqual(p2.counter, 250)
        self.assertEqual(p3.money, 10100)
        self.assertEqual(p3.counter, 225)
        self.assertEqual(p4.money, 9900)
        self.assertEqual(p4.counter, 250)

        self.assertEqual(jp.money, 200)

    def test_call_tripleUp(self):
        """
        トリプルアップモードにおいてコールとフォールドが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        jp = jackpot.Jackpot()
        d = dealer.Dealer()
        p1 = player.Player(1, '1さん')
        p2 = player.Player(2, '2さん')
        p3 = player.Player(3, '3さん')
        p4 = player.Player(4, '4さん')
        players = [p1, p2, p3, p4]

        self.assertEqual(jp.money, 0)

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
            d.pay(c, jp, p)

        for p in players:
            p.updateValue()

        self.assertEqual(p1.money, 10100)
        self.assertEqual(p1.counter, 0)
        self.assertEqual(p2.money, 9900)
        self.assertEqual(p2.counter, 100)
        self.assertEqual(p3.money, 10500) #トリプルアップによって6倍.
        self.assertEqual(p3.counter, 0)
        self.assertEqual(p4.money, 9900)
        self.assertEqual(p4.counter, 100)

        self.assertEqual(jp.money, 200)

    def test_doubt_bluff(self):
        """
        ブラフモードにおいてダウトが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        jp = jackpot.Jackpot()
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
        p18 = player.Player(18, '18さん') #トリプルアップ,的中,コール.
        p19 = player.Player(19, '19さん')
        p20 = player.Player(20, '20さん') #トリプルアップ,的中,フォールド.
        p21 = player.Player(21, '21さん')
        p22 = player.Player(22, '22さん') #トリプルアップ,外れ,コール.
        p23 = player.Player(23, '23さん')
        p24 = player.Player(24, '24さん') #トリプルアップ,外れ,フォールド.
        players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24]

        for p in players:
            p.counter = 300

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
            elif n <= 24: #トリプルアップモード.
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
                p.assign_doubt(players[n])
            else:
                p.assign_doubt(None) #ダウトされる側はダウトしない.

        #detect
        n = 0
        for p in players:
            n += 1
            if n%2 == 1:
                p.detect(jp)

        for p in players:
            d.pay(c, jp, p)

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
        self.assertEqual(p9.money, 9750)
        self.assertEqual(p10.money, 10400)
        self.assertEqual(p11.money, 10200)
        self.assertEqual(p12.money, 10000)
        self.assertEqual(p13.money, 10200)
        self.assertEqual(p14.money, 9800)
        self.assertEqual(p15.money, 9750)
        self.assertEqual(p16.money, 10200)
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
            if n == 12 or n == 16:
                self.assertEqual(p.counter, 250) #カウンターモードでのフォールド.
            elif n%4 == 0:
                self.assertEqual(p.counter, 100) #フォールド.
            else:
                self.assertEqual(p.counter, 225) #コール.

        self.assertEqual(jp.money, 900)

    def test_doubt_counter(self):
        """
        カウンターモードにおいてダウトが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        jp = jackpot.Jackpot()
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
        p18 = player.Player(18, '18さん') #トリプルアップ,的中,コール.
        p19 = player.Player(19, '19さん')
        p20 = player.Player(20, '20さん') #トリプルアップ,的中,フォールド.
        p21 = player.Player(21, '21さん')
        p22 = player.Player(22, '22さん') #トリプルアップ,外れ,コール.
        p23 = player.Player(23, '23さん')
        p24 = player.Player(24, '24さん') #トリプルアップ,外れ,フォールド.
        players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24]

        for p in players:
            p.counter = 300

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
            elif n <= 24: #トリプルアップモード.
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
                p.assign_doubt(players[n])
            else:
                p.assign_doubt(None) #ダウトされる側はダウトしない.

        #detect
        n = 0
        for p in players:
            n += 1
            if n%2 == 1:
                p.detect(jp)

        for p in players:
            d.pay(c, jp, p)

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
        self.assertEqual(p9.money, 9700)
        self.assertEqual(p10.money, 10400)
        self.assertEqual(p11.money, 10200)
        self.assertEqual(p12.money, 10000)
        self.assertEqual(p13.money, 10200)
        self.assertEqual(p14.money, 9800)
        self.assertEqual(p15.money, 9700)
        self.assertEqual(p16.money, 10200)
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
            if n == 12 or n == 16:
                self.assertEqual(p.counter, 250) #カウンターモードでのフォールド.
            elif n%4 == 0:
                self.assertEqual(p.counter, 100) #フォールド.
            else:
                self.assertEqual(p.counter, 225) #コール.

        self.assertEqual(jp.money, 1200)

    def test_doubt_tripleUp(self):
        """
        トリプルアップモードにおいてダウトが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        jp = jackpot.Jackpot()
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
        p18 = player.Player(18, '18さん') #トリプルアップ,的中,コール.
        p19 = player.Player(19, '19さん')
        p20 = player.Player(20, '20さん') #トリプルアップ,的中,フォールド.
        p21 = player.Player(21, '21さん')
        p22 = player.Player(22, '22さん') #トリプルアップ,外れ,コール.
        p23 = player.Player(23, '23さん')
        p24 = player.Player(24, '24さん') #トリプルアップ,外れ,フォールド.
        players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24]

        for p in players:
            p.counter = 300

        #モードの代入.
        n = 0
        for p in players:
            n += 1
            if n%2 == 1: #奇数組はトリプルアップモード.
                p.assign_mode(2)
            elif n <= 8: #ブラフモード.
                p.assign_mode(0)
            elif n <= 16: #カウンターモード.
                p.assign_mode(1)
            elif n <= 24: #トリプルアップモード.
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
                p.assign_doubt(players[n])
            else:
                p.assign_doubt(None) #ダウトされる側はダウトしない.

        #detect
        n = 0
        for p in players:
            n += 1
            if n%2 == 1:
                p.detect(jp)

        for p in players:
            d.pay(c, jp, p)

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
        self.assertEqual(p9.money, 9700)
        self.assertEqual(p10.money, 10400)
        self.assertEqual(p11.money, 10200)
        self.assertEqual(p12.money, 10000)
        self.assertEqual(p13.money, 10200)
        self.assertEqual(p14.money, 9800)
        self.assertEqual(p15.money, 9700)
        self.assertEqual(p16.money, 10200)
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
            if n == 12 or n == 16:
                self.assertEqual(p.counter, 250) #カウンターモードでのフォールド.
            elif n%4 == 0:
                self.assertEqual(p.counter, 100) #フォールド.
            else:
                self.assertEqual(p.counter, 225) #コール.

        self.assertEqual(jp.money, 1200)

    def test_overlap_doubt(self):
        """
        複数のプレイヤーでダウトが重複した場合にダウトが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        jp = jackpot.Jackpot()
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
        p1.assign_doubt(p3)
        p2.assign_doubt(p3)
        p3.assign_doubt(None)
        p4.assign_doubt(p3)

        d.delete_overlap_doubt(players)

        #detect
        for p in players:
            if p.doubt != None:
                p.detect(jp)

        for p in players:
            d.pay(c, jp, p)

        for p in players:
            p.updateValue()

        self.assertEqual(p1.money, 10100)
        self.assertEqual(p2.money, 9800)
        self.assertEqual(p3.money, 9550)
        self.assertEqual(p4.money, 9900)

        self.assertEqual(jp.money, 900)

    def test_duel_success(self):
        """
        デュエル成功時,デュエルが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        jp = jackpot.Jackpot()
        d = dealer.Dealer()
        p1 = player.Player(1, '1さん')
        p2 = player.Player(2, '2さん')
        p3 = player.Player(3, '3さん')
        p4 = player.Player(4, '4さん')
        players = [p1, p2, p3, p4]

        higher = d.return_higher(players)
        lower = d.return_lower(players)
        self.assertEqual(False, d.checkDuel(higher, lower))

        #デュエル成功パターン
        p1.money = 2000
        p2.money = 5000
        p3.money = 10000
        p4.money = 12000

        higher = d.return_higher(players)
        lower = d.return_lower(players)
        if d.checkDuel(higher, lower) == True:
            higher.assign_predict(0)
            c.num = 0
            higher.duel(c, jp, lower)

        self.assertEqual(p1.money, -400)
        self.assertEqual(p2.money, 5000)
        self.assertEqual(p3.money, 10000)
        self.assertEqual(p4.money, 12000)

        self.assertEqual(jp.money, 2400)

    def test_duel_failure(self):
        """
        デュエル失敗時,デュエルが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        jp = jackpot.Jackpot()
        d = dealer.Dealer()
        p1 = player.Player(1, '1さん')
        p2 = player.Player(2, '2さん')
        p3 = player.Player(3, '3さん')
        p4 = player.Player(4, '4さん')
        players = [p1, p2, p3, p4]

        higher = d.return_higher(players)
        lower = d.return_lower(players)
        self.assertEqual(False, d.checkDuel(higher, lower))

        p1.money = 2000
        p2.money = 5000
        p3.money = 10000
        p4.money = 12000

        higher = d.return_higher(players)
        lower = d.return_lower(players)
        if d.checkDuel(higher, lower) == True:
            higher.assign_predict(0)
            c.num = 1
            higher.duel(c, jp, lower)

        self.assertEqual(p1.money, 2000)
        self.assertEqual(p2.money, 5000)
        self.assertEqual(p3.money, 10000)
        self.assertEqual(p4.money, 6000)

        self.assertEqual(jp.money, 6000)

    def test_jackpot(self):
        """
        ジャックポットが正常に行われるかテストする関数.
        """
        #プレイヤーのエントリー.
        c = coin.Coin()
        jp = jackpot.Jackpot()
        d = dealer.Dealer()
        p1 = player.Player(1, '1さん')
        p2 = player.Player(2, '2さん')
        p3 = player.Player(3, '3さん')
        p4 = player.Player(4, '4さん')
        players = [p1, p2, p3, p4]

        jp.money = 10000

        p1.payRatio = 0
        p2.payRatio = 1
        p3.payRatio = 2
        p4.payRatio = 3

        jp.payJP(players)

        self.assertEqual(p1.money, 10000)
        self.assertEqual(p2.money, 11666)
        self.assertEqual(p3.money, 13333)
        self.assertEqual(p4.money, 15000)

        self.assertEqual(jp.money, 1)

if __name__ == '__main__':
    unittest.main()
