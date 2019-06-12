import main, coin, player

class Dealer:

    def entry(self, players):
        """
        名前被りに対応していない.
        """
        for n in range(4):
            print(str(n+1) +'人目の名前を入力してください.')
            name = str(input())
            while name == '':
                print('\u001b[2A\u001b[0J', end='')
                print(str(n+1) +'人目の名前を入力してください.')
                name = str(input())

            p = player.Player(n+1, name)
            players.append(p)

    def announce_state(self, players):
        print('各プレイヤーの所持金とカウンターの値です.')
        for p in players:
            print(str(p.name) +'さん : [所持金 '+ str(p.money) +'] [カウンター '+str(p.counter) +']')

    def announce_bet(self, players):
        print('各プレイヤーの賭けた内容を公表します.')
        for p in players:
            print(str(p.name) +'さん : [モード '+ player.linkMode(p.mode) +'] [賭け金 '+ str(p.bet) +']')

    def announce_call(self, coin, players):
        for p in players:
            if p.call == 1:
                print(p.name +'さん : Call')
            else:
                print(p.name +'さん : Fold')

    def announce_doubt(self, players):
        print('ダウトの結果を公表します.')
        main.pleaseEnter(1)

        count = 0
        for doubter in players:
            count += doubter.doubt
        if count == 0: #count == 0 → 誰もダウトをしていない.
            print('ダウトしたプレイヤーはいませんでした.')

        for doubter in players:
            doubted = main.linkId(doubter.doubt, players)
            if doubted != None:
                print(doubter.name +' → '+ doubted.name)

        main.pleaseEnter(1)

    def detect(self, doubter, doubted):
        """
        指定した相手にダウトを行い,所持金の増減を行う関数.

        引数 :
            doubter : ダウトするプレイヤー.
            douted : ダウトされるプレイヤー.
        """
        if doubted != None:
            doubted.predict -= doubted.bluff
            print('\n'+ doubted.name +'が賭けた面は'+ coin.conversion(doubted.predict)+'でした.')
            if doubted.bluff == 1:
                steal = doubted.bet
                if doubter.mode == 0 and doubted.mode == 2: #奪う額が2倍になる.
                    steal *= 2
                doubted.money -= steal;
                doubter.money += steal;
                print(doubter.name +'のダウトは成功です.'+ str(steal) +'円が'+ doubted.name +'から'+ doubter.name +'へ移動します.')
            else:
                penalty = doubted.bet
                if doubter.mode == 0:
                    penalty = int(penalty/2) #ペナルティが半減する.
                if doubted.mode == 1:
                    penalty += doubted.counter
                doubter.money -= penalty
                print(doubter.name +'のダウトは失敗です.ペナルティとして'+ str(penalty) +'円を没収します.')
            main.pleaseEnter(1)

    def pay(self, coin, player):
        """
        お金を清算する関数
        """
        if player.predict%2 == coin.num:
            rate = 2
            if player.mode == 2:
                rate = 3
            player.money += player.bet*rate;
            print(player.name +'へ'+ str(player.bet*rate) +'円をお支払いします.')
        else:
            print('残念ですが'+ player.name +'の賭金は没収となります.')

    def checkFinish(self, players):
        """
        各プレイヤーの所持金が0になったか確認する関数.
        """
        finish = False
        for p in players:
            if p.money <= 0:
                finish = True
        return finish

    def finishGame(self, players):
        """
        最も所持金の多いプレイヤーを勝者とする関数.
        全員が負けた時には対応していない.
        """
        print('\n-- FinishGame --')
        self.announce_state(players)
        print('') #空白行

        winners = []
        losers = []
        maxim = 0 #所持金の最大値
        for p in players:
            if p.money <= 0: #所持金が0になった時
                losers.append(p)
            elif p.money > maxim: #最大値更新時
                winners.clear()
                winners.append(p)
                maxim = p.money
            elif p.money == maxim: #同率時
                winners.append(p)

        for loser in losers:
            print(loser.name +'さん', end='')
        print('の所持金が無くなりました.')
        for winner in winners:
            print(winner.name +'さん', end='')
        print('の勝利です!')

    #以下,標準出力を使った関数のテストが面倒臭いがために作ったテスト用関数。
    def test_announce_doubt(self, players):
        print('ダウトの結果を公表します.')

        count = 0
        for doubter in players:
            count += doubter.doubt
        if count == 0: #count == 0 → 誰もダウトをしていない.
            print('ダウトしたプレイヤーはいませんでした.')

        for doubter in players:
            doubted = main.linkId(doubter.doubt, players)
            if doubted != None:
                print(doubter.name +' → '+ doubted.name)

    def test_detect(self, doubter, doubted):
        if doubted != None:
            doubted.predict -= doubted.bluff
            print('\n'+ doubted.name +'が賭けた面は'+ coin.conversion(doubted.predict)+'でした.')
            if doubted.bluff == 1:
                steal = doubted.bet
                if doubter.mode == 0 and doubted.mode == 2: #奪う額が2倍になる.
                    steal *= 2
                doubted.money -= steal;
                doubter.money += steal;
                print(doubter.name +'のダウトは成功です.'+ str(steal) +'円が'+ doubted.name +'から'+ doubter.name +'へ移動します.')
            else:
                penalty = doubted.bet
                if doubter.mode == 0:
                    penalty = int(penalty/2) #ペナルティが半減する.
                if doubted.mode == 1:
                    penalty += doubted.counter
                doubter.money -= penalty
                print(doubter.name +'のダウトは失敗です.ペナルティとして'+ str(penalty) +'円を没収します.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
