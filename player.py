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

    def input_mode(self):
        """
        モードを標準入力する関数.
        """
        print('モードを選択してください.', end='')
        print('(ブラフ, カウンター, ダブルアップ, デュエル)')
        mode = None #選択されたモード.
        while True:
            select = input()
            if select == 'ブラフ':
                mode = 0
                break
            elif select == 'カウンター':
                mode = 1
                break
            elif select == 'ダブルアップ':
                mode = 2
                break
            elif select == 'デュエル':
                mode = 3
                break
            else:
                print('\u001b[2A\u001b[0J', end='')
                print('もう一度入力してください.', end='')
                print('(ブラフ, カウンター, ダブルアップ, デュエル)')
                continue
        return mode

    def assign_mode(self, mode):
        """
        モードを代入する関数.
        """
        self.mode = mode

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

    def input_doubt(self, players):
        """
        ダウトする相手を標準入力する関数.
        """
        print('どのプレイヤーをダウトしますか？', end='')
        print('('+ str(players[0].name) +', '+ str(players[1].name) +', '+ str(players[2].name) +', ダウトしない)')
        doubt = None
        doubtName = ''
        while True:
            doubtName = input()
            if doubtName == players[0].name:
                doubt = players[0].playerNo
                break
            elif doubtName == players[1].name:
                doubt = players[1].playerNo
                break
            elif doubtName == players[2].name:
                doubt = players[2].playerNo
                break
            elif doubtName == 'ダウトしない':
                doubt = 0
                break
            else:
                print('\u001b[2A\u001b[0J', end='')
                print('もう一度入力してください.', end='')
                print('('+ str(players[0].name) +', '+ str(players[1].name) +', '+ str(players[2].name) +', ダウトしない)')
                continue
        if doubt != 0:
            print(doubtName +'さんをダウトします.')
        else:
            print('ダウトしません.')
        return doubt

    def assign_doubt(self, doubt):
        """
        ダウトする相手を代入する関数.
        """
        self.doubt = doubt

    def detect(self, players):
        """
        指定した相手にダウトを行い,所持金の増減を行う関数.
        linkId()の消去に伴ってリファクタリング予定.
        """
        doubted = main.linkId(self.doubt, players)
        doubted.predict -= doubted.bluff #douted.predictを本来の結果に戻す.
        print('\n'+ doubted.name +'が賭けた面は'+ coin.conversion(doubted.predict)+'でした.')

        bonus = doubted.bet
        penalty = doubted.bet
        if doubted.bluff == 1: #ダウト成功.
            if self.mode == 0 and doubted.mode == 2: #奪う額が2倍になる.
                bonus *= 2
                penalty *= 2
            if doubted.mode == 0: #ペナルティが半減.
                penalty = int(penalty/2);
            self.money += bonus
            doubted.money -= penalty;

            print(self.name +'のダウトは成功です.')
            print('ダウト成功のボーナスとして'+ self.name +'さんへ'+ str(bonus) +'円をお支払いします.')
            print('ブラフ失敗のペナルティとして'+ doubted.name +'さんから'+ str(penalty) +'円を没収します.')

        else: #ダウト失敗.
            if self.mode == 0:
                penalty = int(penalty/2) #ペナルティが半減する.
            self.money -= penalty
            print(self.name +'のダウトは失敗です.')
            print('ダウト失敗のペナルティとして'+ self.name +'さんから'+ str(penalty) +'円を没収します.')
            if doubted.mode == 1:
                doubted.counterAttack(doubted)

    def counterAttack(self, doubter):
        doubter.money -= self.counter
        self.money += self.counter
        print('さらに'+ str(self.counter) +'円が'+ doubter.name +'から'+ self.name +'へ移動します.')

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
        modeName = 'ダブルアップ'
    return modeName

if __name__ == '__main__':
    import doctest
    doctest.testmod()
