import main, coin, player, Bot

class Dealer:
    minimumBet = 0
    minimumRate = 0.08

    def entry_num(self):
        """
        参加人数を決定する関数.
        int型以外の入力と1以下の入力は弾く.
        """
        print('参加人数を入力してください')
        while True:
            try:
                num = int(input())
            except ValueError: #int型以外を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('int型で入力してください.')
                continue
            if 1 < num:
                print(str(num) +'人でゲームを始めます.')
                break
            else: #1以下を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('それではゲームを始められません.')
        return num

    def naming(self, players, playerNo):
        """
        プレイヤーの名前を入力する関数.
        """
        print(str(playerNo) +'人目の名前を入力してください.')
        name = str(input())
        while name == '':
            print('\u001b[2A\u001b[0J', end='')
            print(str(playerNo) +'人目の名前を入力してください.')
            name = str(input())

        return name

    def entry(self, players, playerNo, name):
        """
        プレイヤーを参加させる関数.
        """
        p = player.Player(playerNo, name)
        players.append(p)

    def entryBot(self, players, playerNo, name):
        """
        プレイヤーを参加させる関数.
        """
        p = Bot.Bot(playerNo, name)
        players.append(p)

    def announce_state(self, players):
        print('各プレイヤーの所持金とカウンターの値です.')
        for p in players:
            print(str(p.name) +'さん : [所持金 '+ str(p.money) +'] [カウンター '+ str(p.counter) +']')

    def announce_bet(self, players):
        print('各プレイヤーの賭けた内容を公表します.')
        for p in players:
            betRate = int(p.betRate*100)
            print(str(p.name) +'さん : [賭け金 '+ str(p.bet) +' ('+str(betRate)+'%)] [所持金 '+str(p.money) +']')

    def announce_call(self, coin, players):
        for p in players:
            if p.isCall == True:
                print(p.name +'さん : Call')
            else:
                print(p.name +'さん : Fold')

    def announce_mode(self, players):
        print('各プレイヤーのモードを公表します.')
        for p in players:
            print(str(p.name) +'さん : [モード '+ p.mode +']')

    def announce_doubt(self, players):
        print('ダウトの結果を公表します.')
        main.pleaseEnter(1)

        #誰もダウトをしていない場合の処理.
        #誰かがダウトしている場合はこの処理はすり抜ける.
        count = 0
        for doubter in players:
            if doubter.doubt != None:
                count += 1
        if count == 0: #count == 0 → 誰もダウトをしていない.
            print('ダウトしたプレイヤーはいませんでした.')

        #誰かがダウトした場合の処理.
        #誰もダウトをしていない場合はこの処理はすり抜ける.
        for doubter in players:
            doubted = doubter.doubt
            if doubted != None:
                print(doubter.name +' → '+ doubted.name)

    def calcMinimum(self, players):
        """
        self.minimumBetとself.minimumRateを計算する関数.
        """
        #self.minimumRateの計算.
        self.minimumRate += 0.02
        if self.minimumRate > 0.5: #上限は5割まで.
            self.minimumRate = 0.5

        #self.minimumBetの計算.
        #self.minimumBetは最も所持金の多いプレイヤーの所持金に依存する.
        higher = self.return_higher(players) #最も所持金の多いプレイヤーを代入.
        self.minimumBet = int(higher.money * self.minimumRate)

    def delete_overlap_doubt(self, players):
        """
        複数のプレイヤーで重複したダウトを消す関数.
        重複した場合,所持金の低いプレイヤーのダウトが優先される.
        """
        for p in players:
            doubters = [] #自分を疑っているプレイヤー.
            for doubter in players:
                doubted = doubter.doubt
                if doubted == p: #もし自分を疑っている場合
                    doubters.append(doubter)

            lowest = None
            minimum = float('inf') #無限
            for doubter in doubters:
                doubter.doubt = None #一旦全員のplayer.doubtをNoneにする.
                if doubter.money < minimum: #所持金の低いプレイヤーが優先.
                    lowest = doubter
                    minimum = doubter.money
            if lowest != None: #最も所持金の低いプレイヤーのみがダウトできる.
                lowest.doubt = p #lowestのplayer.doubtを再設定.

    def pay(self, coin, player):
        """
        お金を清算する関数.
        """
        rate = 2
        if player.predict == coin.num: #予想が的中した場合(嘘含む).
            if player.mode == 'トリプルアップ' and player.isCall == True and player.bluff == 1: #トリプルアップ適用.
                rate *= 3
                print('トリプルアップ成功です.', end='')
            bonus = player.bet*rate #勝利金
            player.money += bonus
            print(player.name +'へ'+ str(bonus) +'円をお支払いします.')
        else:
            print('残念ですが'+ player.name +'の賭金は没収となります.')

    def return_higher(self, players):
        """
        最も所持金の高いプレイヤーを返す関数.
        """
        higher = None
        maximum = 0
        for p in players:
            if p.money > maximum:
                maximum = p.money
                higher = p
        return higher

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
        main.pleaseEnter(1)
        print('') #空白行

        winners = [] #同率1位を考慮してリスト型.
        losers = [] #複数人飛んだ時を考慮してリスト型.
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
