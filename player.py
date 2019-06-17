import coin, main, math

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
    doubt = None #ダウト先のプレイヤー.

    def __init__(self, playerNo, name):
        self.playerNo = playerNo
        self.name = name

    def input_mode(self):
        """
        モードを標準入力する関数.
        """
        choices = ['ブラフ', 'カウンター', 'ダブルアップ']
        print('モードを選択してください.', end='')
        print_choices(choices)
        mode = answer(choices) #入力
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
        choices = ['表', '裏']
        print('どちらに賭けますか？', end='')
        print_choices(choices)
        predict = answer(choices) #入力
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
        limmit = math.ceil(self.money/3) #賭け金の上限額.所持金の3分の1.小数点は切り上げ.
        print('いくら賭けますか？', end='')
        while True:
            print('(現在の所持金'+ str(self.money) +'円)(上限'+ str(limmit) +'円)')
            try:
                ans = int(input())
            except ValueError: #int型以外を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('int型で入力してください.', end='')
                continue
            if 0 < ans and ans <= limmit:
                break
            elif ans <= 0: #0以下を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('それでは賭けになりません.', end='')
            else: #所持金を超えた額を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('賭け金が上限を超えています.', end='')
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

    def input_call(self, c_num):
        """
        コイントスの結果と予想を判定して、コールかフォールドを標準入力する関数.

        引数 :
            c_num : コインの表裏を示す.0は表,1は裏に対応している.

        返り値 :
            call : コールなら0,フォールドなら1が入る.
        """
        choices = ['Call', 'Fold']
        if self.predict == c_num: #プレイヤーの予想とコインが一致してるかの判定
            print('予想が的中しました.', end='')
        else:
            print('予想が外れました.', end='')
        print_choices(choices)
        call = answer(choices) #入力
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
        choices = []
        for p in players:
            choices.append(p.name)
        choices.append('ダウトしない')
        print('どのプレイヤーをダウトしますか？', end='')
        print_choices(choices)
        ans = answer(choices) #入力
        if ans == len(choices)-1:
            print('ダウトしません.')
        else:
            doubt = players[ans]
            print(doubt.name +'さんをダウトします.')
        return doubt

    def assign_doubt(self, doubt):
        """
        ダウトする相手を代入する関数.
        """
        self.doubt = doubt

    def detect(self):
        """
        指定した相手にダウトを行い,所持金の増減を行う関数.
        linkId()の消去に伴ってリファクタリング予定.
        """
        doubt = self.doubt
        doubt.predict -= doubt.bluff #doubt.predictを本来の結果に戻す.
        print('\n'+ doubt.name +'が賭けた面は'+ coin.conversion(doubt.predict)+'でした.')

        bonus = doubt.bet
        penalty = doubt.bet
        if doubt.bluff == 1: #ダウト成功.
            if self.mode == 0 and doubt.mode == 2: #奪う額が2倍になる.
                bonus *= 2
                penalty *= 2
            if doubt.mode == 0: #ペナルティが半減.
                penalty = int(penalty/2);
            self.money += bonus
            doubt.money -= penalty;

            print(self.name +'のダウトは成功です.')
            print('ダウト成功のボーナスとして'+ self.name +'さんへ'+ str(bonus) +'円をお支払いします.')
            print('ブラフ失敗のペナルティとして'+ doubt.name +'さんから'+ str(penalty) +'円を没収します.')

        else: #ダウト失敗.
            if self.mode == 0:
                penalty = int(penalty/2) #ペナルティが半減する.
            self.money -= penalty
            print(self.name +'のダウトは失敗です.')
            print('ダウト失敗のペナルティとして'+ self.name +'さんから'+ str(penalty) +'円を没収します.')
            if doubt.mode == 1:
                doubt.counterAttack(self)

    def counterAttack(self, doubter):
        """
        カウンターを実行する関数.
        """
        doubter.money -= self.counter
        self.money += self.counter
        print('さらにカウンターにより'+ str(self.counter) +'円が'+ doubter.name +'から'+ self.name +'へ移動します.')

    def duel(self, c, lower):
        """
        デュエルを行う関数.
        """
        if self.predict == c.num:
            steal = int(self.money/5)
            self.money += steal
            lower.money -= steal
            print('予想が的中しました.'+ str(steal) +'円が'+ lower.name +'から'+ self.name +'へ移動します.')
        else:
            steal = int(self.money/2)
            self.money -= steal
            lower.money += steal
            print('予想が外れました.'+ str(steal) +'円が'+ self.name +'から'+ lower.name +'へ移動します.')
        self.predict = 0

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
        self.doubt = None

    def yourTurn(self):
        print(str(self.name) +'さんのターンです.')
        main.pleaseEnter(1)

def answer(choices):
    """
    標準入力で選択肢を選ぶ関数.

    引数 :
        choices : 選択肢のリスト.str型.

    返り値 :
        ans : choicesのインデックスが返る.
    """
    ans = None
    while True: #ちゃんとした入力がされるまで永遠に質問する.
        str = input()
        n = 0
        for choice in choices:
            if str == choice:
                ans = n
                return ans
            else:
                n += 1
        print('\u001b[2A\u001b[0J', end='')
        print('もう一度入力してください.', end='')
        print_choices(choices)

def print_choices(choices):
    """
    標準入力系の関数で選択肢をプリントする関数.
    """
    print('(', end='')
    for choice in choices:
        print(str(choice), end='')
        if choice != choices[-1]:
            print(', ', end='')
    print(')')

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
