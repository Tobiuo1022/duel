import coin, main

class Player:
    playerNo = 0 #プレイヤーの番号.
    name = '' #プレイヤーの名前.
    money = 10000 #所持金.
    counter = 0 #カウンターの値
    mode = None #選択したモード
    predict = 0 #予想した面.
    bet = 0 #賭け金
    isCall = False #通常はFalse,コールするならTrueが入る.
    bluff = 0 #通常は0,嘘をつくと1が入る.
    doubt = 0 #ダウト先のプレイヤー.
    target = 0 #デュエルを宣言するプレイヤー.

    def __init__(self, playerNo, name):
        self.playerNo = playerNo
        self.name = name

    def selectMode(self):
        """
        モードを選択する関数.
        後々消す予定.
        """
        print(str(self.name) +'さん')
        main.pleaseEnter(1)
        print('モードを選択してください.', end='')
        print('(ブラフ, カウンター, トリプルアップ, デュエル)')
        while True:
            select = input()
            if select == 'ブラフ':
                self.mode = 0
                break
            elif select == 'カウンター':
                self.mode = 1
                break
            elif select == 'トリプルアップ':
                self.mode = 2
                break
            elif select == 'デュエル':
                self.mode = 3
                break
            else:
                print('\u001b[2A\u001b[0J', end='')
                print('もう一度入力してください.', end='')
                print('(ブラフ, カウンター, トリプルアップ, デュエル)')
                continue

    def input_mode(self):
        """
        モードを標準入力する関数.
        """
        print('モードを選択してください.', end='')
        print('(ブラフ, カウンター, トリプルアップ, デュエル)')
        mode = None #選択されたモード.
        while True:
            select = input()
            if select == 'ブラフ':
                mode = 0
                break
            elif select == 'カウンター':
                mode = 1
                break
            elif select == 'トリプルアップ':
                mode = 2
                break
            elif select == 'デュエル':
                mode = 3
                break
            else:
                print('\u001b[2A\u001b[0J', end='')
                print('もう一度入力してください.', end='')
                print('(ブラフ, カウンター, トリプルアップ, デュエル)')
                continue
        return mode

    def assign_mode(self, mode):
        """
        モードを代入する関数.
        """
        self.mode = mode

    def betting(self):
        """
        コイントスの結果を予想して所持金を賭ける関数.
        のちのち消す予定.
        """
        print('どちらに賭けますか？(表, 裏)')
        self.predict = self.answer('表', '裏') #入力

        print('いくら賭けますか？(現在の所持金'+ str(self.money) +'円)')
        self.bet = self.inputBet() #入力

        self.money -= self.bet
        print(coin.conversion(self.predict) +'に'+ str(self.bet) +'円を賭けました.')
        main.pleaseEnter(9)

    def input_predict(self):
        """
        コイントスの予想を標準入力する関数.
        """
        print('どちらに賭けますか？(表, 裏)')
        predict = self.answer('表', '裏') #入力
        return predict

    def assign_predict(self, predict):
        """
        コイントスの予想を代入する関数.
        """
        self.predict = predict

    def input_bet(self):
        """
        賭け金を標準入力する関数.
        """
        print('いくら賭けますか？(現在の所持金'+ str(self.money) +'円)')
        while True:
            try:
                ans = int(input())
            except ValueError: #int型以外を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('int型で入力してください.(現在の所持金'+ str(self.money) +'円)')
                continue
            if 0 < ans and ans <= self.money:
                break
            elif ans <= 0: #0以下を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('それでは賭けになりません.(現在の所持金'+ str(self.money) +'円)')
            else: #所持金を超えた額を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('賭け金が所持金を超えています.(現在の所持金'+ str(self.money) +'円)')
        return ans

    def assign_bet(self, bet):
        """
        賭け金を代入する関数.
        """
        self.bet = bet
        self.money -= bet

    def print_bet(self):
        """
        ベットの内容をプリントする関数.
        """
        print(coin.conversion(self.predict) +'に'+ str(self.bet) +'円を賭けました.')

    def inputTarget(self, players):
        print('どのプレイヤーにデュエルを宣言しますか？', end='')
        print('('+ str(players[0].name) +', '+ str(players[1].name) +', '+ str(players[2].name)+ ')')
        targetName = ''
        while True:
            targetName = input()
            if targetName == players[0].name:
                self.target = players[0].playerNo
                break
            elif targetName == players[1].name:
                self.target = players[1].playerNo
                break
            elif targetName == players[2].name:
                self.target = players[2].playerNo
                break
            else:
                print('\u001b[2A\u001b[0J', end='')
                print('もう一度入力してください.', end='')
                print('('+ str(players[0].name) +', '+ str(players[1].name) +', '+ str(players[2].name)+ ')')
                continue
        print(targetName +'さんにデュエルを宣言します.')
        main.pleaseEnter(7)

    def callOrFold(self, coin):
        """
        コイントスの結果と予想を判定して、降りるか降りないかを決める関数.
        降りる降りないの順番が逆になっているので注意.
        後々消す予定.
        """
        print(str(self.name) +'さん')
        main.pleaseEnter(1)
        if self.predict == coin.num: #プレイヤーの予想とコインが一致してるかの判定
            print('予想が的中しました.(降りる, 降りない)')
            ans = self.answer('降りる', '降りない')
            if ans == 0: #的中しているが降りる.
                self.bluff = 1
                self.predict += self.bluff
                self.isCall = False
            else: #的中し,コールする.
                self.bluff = 0
                self.isCall = True
        else:
            print('予想が外れました.(降りる, 降りない)')
            ans = self.answer('降りる', '降りない')
            if ans == 0: #外し,降りる.
                self.bluff = 0
                self.isCall = False
            else: #外したがコールする.
                self.bluff = 1
                self.predict += self.bluff
                self.isCall = True
        main.pleaseEnter(4)

    def input_call(self, c_num):
        """
        コイントスの結果と予想を判定して、コールかフォールドを標準入力する関数.

        引数 :
            c_num : コインの表裏を示す.0は表,1は裏に対応している.

        返り値 :
            call : コールなら0,フォールドなら1が入る.
        """
        if self.predict == c_num: #プレイヤーの予想とコインが一致してるかの判定
            print('予想が的中しました.(Call, Fold)')
        else:
            print('予想が外れました.(Call, Fold)')
        call = self.answer('Call', 'Fold')
        return call

    def assign_call(self, c_num, call):
        """
        コイントスの結果と予想を判定して、コールかフォールドを標準入力する関数.

        引数 :
            c_num : コインの表裏を示す.0は表,1は裏に対応している.
        """
        if self.predict == c_num: #プレイヤーの予想とコインが一致してるかの判定
            if call == 0: #的中し,コールする.
                self.bluff = 0
                self.isCall = True
            else: #的中しているが降りる.
                self.bluff = 1
        else:
            if call == 0: #外したがコールする.
                self.bluff = 1
                self.isCall = True
            else: #外し,降りる.
                self.bluff = 0
        self.predict = (self.predict + self.bluff)%2 #嘘をついた場合,self.predictがひっくり返る.

    def print_call(self):
        """
        コールの内容をプリントする関数.
        メッセージの内容は未定.
        """
        pass

    def counterAttack(self, douter):
        doubter.money -= self.counter
        self.money += self.couter
        print('さらに'+ str(self.couter) +'円が'+ doubter.name +'から'+ self.name +'へ移動します.')

    def duel(self, coin, players):
        target = main.linkId(self.target, players)
        print(self.name +'さんが'+ target.name +'さんへデュエルを宣言しました.')
        print('各プレイヤーのBetPhaseの内容を破棄し,DuelPhaseへ移行します.')
        print(self.name +'さん,どちらに賭けますか？(表, 裏)')
        self.predict = self.answer('表', '裏') #入力
        coin.toss()
        main.pleaseEnter(1)
        print('')
        if self.predict == coin.num:
            steal = int(self.money/10)
            self.money += steal
            target.money -= steal
            print('予想が的中しました.'+ str(steal) +'円が'+ target.name +'から'+ self.name +'へ移動します.')
        else:
            steal = int(self.money/2)
            self.money -= steal
            target.money += steal
            print('予想が外れました.'+ str(steal) +'円が'+ self.name +'から'+ target.name +'へ移動します.')
        self.predict = 0

    def answer(self, zero, first):
        """
        コインの表裏やYesとNoを標準入力するための関数.

        引数 :
            zero : 表もしくはYが対応.
            first : 裏もしくはNが対応.

        返り値 :
            ans : 0か1で返る.
        """
        ans = 0
        while True: #ちゃんとした入力がされるまで永遠に質問する.
            str = input()
            if str == zero:
                break
            elif str == first:
                ans = 1
                break
            else:
                print('\u001b[2A\u001b[0J', end='')
                print(zero + 'もしくは' + first + 'でお答えください.')
        return ans

    def inputBet(self):
        """
        賭け金を標準入力するための関数.
        後々消す予定.
        """
        while True:
            try:
                ans = int(input())
            except ValueError: #int型以外を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('int型で入力してください.(現在の所持金'+ str(self.money) +'円)')
                continue
            if 0 < ans and ans <= self.money:
                break
            elif ans <= 0: #0以下を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('それでは賭けになりません.(現在の所持金'+ str(self.money) +'円)')
            else: #所持金を超えた額を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('賭け金が所持金を超えています.(現在の所持金'+ str(self.money) +'円)')
        return ans

    def inputDoubt(self, players):
        """
        任意のプレイヤーをダウトするための関数.
        """
        print(str(self.name) +'さん')
        main.pleaseEnter(1)
        print('どのプレイヤーをダウトしますか？', end='')
        print('('+ str(players[0].name) +', '+ str(players[1].name) +', '+ str(players[2].name) +', ダウトしない)')
        doubtName = ''
        while True:
            doubtName = input()
            if doubtName == players[0].name:
                self.doubt = players[0].playerNo
                break
            elif doubtName == players[1].name:
                self.doubt = players[1].playerNo
                break
            elif doubtName == players[2].name:
                self.doubt = players[2].playerNo
                break
            elif doubtName == 'ダウトしない':
                self.doubt = 0
                break
            else:
                print('\u001b[2A\u001b[0J', end='')
                print('もう一度入力してください.', end='')
                print('('+ str(players[0].name) +', '+ str(players[1].name) +', '+ str(players[2].name) +', ダウトしない)')
                continue
        if self.doubt != 0:
            print(doubtName +'さんをダウトします.')
        else:
            print('ダウトしません.')
        main.pleaseEnter(5)

    def updateValue(self):
        """
        各プレイヤーの持っている値をリセットする.
        カウンターは更新する.
        """
        if self.isCall == False:
            self.counter = int(self.bet/2)
        else:
            self.counter = int(self.counter/2)
        self.mode = None
        self.predict = 0
        self.bet = 0
        self.isCall = False
        self.bluff = 0
        self.doubt = 0

    def yourTurn(self):
        print(str(self.name) +'さんのターンです.')
        main.pleaseEnter(1)

    #以下,標準出力を使った関数のテストが面倒臭いがために作ったテスト用関数。
    def test_betting(self, face, bet):
        """
        引数 :
            face : 表は0,裏は1.
            bet : 賭ける額.
        """
        self.predict = face
        self.bet = bet
        self.money -= self.bet

    def test_callOrFold(self, coin, ans):
        """
        引数 :
            ans : 降りるなら0,降りないなら1が入る.
        """
        if self.predict == coin.num: #プレイヤーの予想とコインが一致してるかの判定
            if ans == 0: #的中しているが降りる.
                self.bluff = 1
                self.predict += self.bluff
                self.isCall = False
            else: #的中し,コールする.
                self.bluff = 0
                self.isCall = True
        else:
            if ans == 0: #外し,降りる.
                self.bluff = 0
                self.isCall = False
            else: #外したがコールする.
                self.bluff = 1
                self.predict += self.bluff
                self.isCall = True

    def test_duel(self, coin, players, correct):
        """
        引数 :
            correct : コインの表裏の予想の結果.的中ならTrue,外れならFalseが入る.
        """
        target = main.linkId(self.target, players)
        if correct:
            steal = int(self.money/10)
            self.money += steal
            target.money -= steal
        else:
            steal = int(self.money/2)
            self.money -= steal
            target.money += steal

def linkMode(mode):
    """
    modeの数字をカタカナで返す.変換器.
    """
    modeName = None
    if mode == 0:
        modeName = 'ブラフ'
    elif mode == 1:
        modeName = 'カウンター'
    elif mode == 2:
        modeName = 'トリプルアップ'
    return modeName

if __name__ == '__main__':
    import doctest
    doctest.testmod()
