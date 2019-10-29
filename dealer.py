import main, coin, player

class Dealer:
    minimumBet = 0
    minimumRate = 0.05

    def entry_num(self):
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

    def entry(self, players, num):
        """
        名前被りに対応していない.
        """
        for n in range(num):
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
            print(str(p.name) +'さん : [モード '+ p.mode +']')

    def announce_doubt(self, players):
        print('ダウトの結果を公表します.')
        main.pleaseEnter(1)

        count = 0
        for doubter in players:
            if doubter.doubt != None:
                count += 1
        if count == 0: #count == 0 → 誰もダウトをしていない.
            print('ダウトしたプレイヤーはいませんでした.')

        for doubter in players:
            doubted = doubter.doubt
            if doubted != None:
                print(doubter.name +' → '+ doubted.name)

    def calcMinimum(self, players):
        self.minimumRate += 0.05
        if self.minimumRate > 0.5: #上限は5割まで.
            self.minimumRate = 0.5

        higher = self.return_higher(players)
        minimum = int(higher.money * self.minimumRate)
        self.minimumBet = minimum

    def delete_overlap_doubt(self, players):
        """
        複数のプレイヤーで重複したダウトを消す関数.
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
                doubter.doubt = None #一旦全員のダウトを0にする.
                if doubter.money < minimum: #所持金の低いプレイヤーが優先.
                    lowest = doubter
                    minimum = doubter.money
            if lowest != None: #最も所持金の低いプレイヤーのみがダウトできる.
                lowest.doubt = p

    def pay(self, c, p):
        """
        お金を清算する関数.
        """
        rate = 2
        if p.predict == c.num: #予想が的中した場合(嘘含む).
            if p.mode == 'トリプルアップ' and p.isCall == True and p.bluff == 1: #トリプルアップ適用.
                rate *= 3
                print('トリプルアップ成功です.', end='')
            bonus = p.bet*rate #勝利金
            p.money += bonus
            print(p.name +'へ'+ str(bonus) +'円をお支払いします.')
        else:
            print('残念ですが'+ p.name +'の賭金は没収となります.')

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

    def return_lower(self, players):
        """
        最も所持金の低いプレイヤーを返す関数.
        """
        lower = None
        minimum = float('inf') #無限
        for p in players:
            if p.money <= minimum:
                minimum = p.money
                lower = p
        return lower

    def checkDuel(self, higher, lower):
        """
        デュエルが行われるか確認する関数.
        """
        if higher.money >= lower.money*3: #所持金の差が3倍以上ならTrueを返す.
            higher.target = lower
            return True
        else:
            return False

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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
