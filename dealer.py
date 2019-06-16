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
            print(str(p.name) +'さん : [所持金 '+ str(p.money) +'] [カウンター '+ str(p.counter) +']')

    def announce_bet(self, players):
        print('各プレイヤーの賭けた内容を公表します.')
        for p in players:
            print(str(p.name) +'さん : [賭け金 '+ str(p.bet) +'] [所持金 '+str(p.money) +']')

    def announce_call(self, coin, players):
        for p in players:
            if p.isCall == True:
                print(p.name +'さん : Call')
            else:
                print(p.name +'さん : Fold')

    def announce_mode(self, players):
        print('各プレイヤーのモードを公表します.')
        for p in players:
            print(str(p.name) +'さん : [モード '+ player.linkMode(p.mode) +']')

    def announce_doubt(self, players):
        print('ダウトの結果を公表します.')
        main.pleaseEnter(1)

        count = 0
        for doubter in players:
            count += doubter.doubt
        if count == 0: #count == 0 → 誰もダウトをしていない.
            print('ダウトしたプレイヤーはいませんでした.')

        for p in players:
            lowest = None
            minimum = float('inf') #無限
            for doubter in players:
                doubted = main.linkId(doubter.doubt, players)
                if doubted == p: #もし自分を疑っている場合
                    if doubter.money < minimum: #所持金の低いプレイヤーが優先.
                        minimum = doubter.money
                        lowest = doubter
                    doubter.doubt = 0 #所持金の低くないプレイヤーはダウトできなくなる.
            if lowest != None:
                lowest.doubt = p.playerNo

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
            bonus = doubted.bet
            penalty = doubted.bet
            if doubted.bluff == 1:
                if doubter.mode == 0 and doubted.mode == 2: #奪う額が2倍になる.
                    bonus *= 2
                    penalty *= 2
                if doubted.mode == 0: #ペナルティが半減.
                    doubted.money -= int(penalty/2);
                doubter.money += bonus
                doubted.money -= penalty;
                print(doubter.name +'のダウトは成功です.')
                print('ボーナスとして'+ doubter.name +'さんへ'+ str(bonus) +'円をお支払いします.')
                print('ブラフ失敗のペナルティとして'+ doubted.name +'から'+ str(penalty) +'円を没収します.')
            else:
                if doubter.mode == 0:
                    penalty = int(penalty/2) #ペナルティが半減する.
                doubter.money -= penalty
                print(doubter.name +'のダウトは失敗です.')
                print('ペナルティとして'+ str(penalty) +'円を没収します.')
                if doubted.mode == 1:
                    douted.couterAttack(doubter)
            main.pleaseEnter(1)

    def pay(self, c, player):
        """
        お金を清算する関数.
        """
        rate = 2
        if player.predict == c.num: #予想が的中した場合(嘘含む).
            bonus = player.bet*rate #勝利金
            player.money += bonus
            print(player.name +'へ'+ str(bonus) +'円をお支払いします.')
        else:
            print('残念ですが'+ player.name +'の賭金は没収となります.')

    def checkDuel(self, players):
        declarer = None
        maximum = 0
        for p in players:
            if p.mode == 3:
                if p.money > maximum: #所持金の高いプレイヤーが優先.
                    maximum = p.money
                    declarer = p
        return declarer

    def resetValue(self, players):
        for p in players:
            p.money += p.bet
            p.mode = 0
            p.bet = 0
            p.predict = 0

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
        maximum = 0 #所持金の最大値
        for p in players:
            if p.money <= 0: #所持金が0になった時
                losers.append(p)
            elif p.money > maximum: #最大値更新時
                winners.clear()
                winners.append(p)
                maximum = p.money
            elif p.money == maximum: #同率時
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

        for p in players:
            lowest = None
            minimum = float('inf') #無限
            for doubter in players:
                doubted = main.linkId(doubter.doubt, players)
                if doubted == p: #もし自分を疑っている場合
                    if doubter.money < minimum: #所持金の低いプレイヤーが優先.
                        minimum = doubter.money
                        lowest = doubter
                    doubter.doubt = 0 #所持金の低くないプレイヤーはダウトできなくなる.
            if lowest != None:
                lowest.doubt = p.playerNo

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
