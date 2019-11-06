import main, coin, jackpot, math

class Player:
    playerNo = 0 #プレイヤーの番号.
    name = '' #プレイヤーの名前.
    money = 10000 #所持金.
    counter = 0 #カウンターの値
    hands = [] #モードの手札.
    mode = None #選択したモード
    predict = 0 #予想した面.
    bet = 0 #賭け金
    betRate = 0
    isCall = False #通常はFalse,コールするならTrueが入る.
    bluff = 0 #通常は0,嘘をつくと1が入る.
    doubt = None #ダウト先のプレイヤー.

    def __init__(self, playerNo, name):
        self.playerNo = playerNo
        self.name = name
        self.hands = []

    def input_mode(self):
        """
        モードを標準入力する関数.
        """
        choices = self.hands
        print('モードを選択してください.', end='')
        print_choices(choices)
        ans = select(choices) #入力
        mode = self.hands.pop(ans-1)
        return mode

    def assign_mode(self, mode):
        """
        モードを代入する関数.
        """
        self.mode = mode

    def print_mode(self):
        """
        ベットの内容をプリントする関数.
        """
        print(self.mode +'を選択しました.')

    def input_predict(self):
        """
        コイントスの予想を標準入力する関数.
        """
        choices = ['表', '裏']
        print('どちらに賭けますか？', end='')
        print_choices(choices)
        predict = select(choices)-1 #入力
        return predict

    def assign_predict(self, predict):
        """
        コイントスの予想を代入する関数.
        """
        self.predict = predict

    def input_minimum(self, minimumBet):
        """
        所持金が最低額に達してない時の関数.
        """
        print('所持金が最低額に達していないので全額を賭けます.')
        bet = self.money
        return bet

    def input_bet(self, minimumBet):
        """
        賭け金を標準入力する関数.
        入力がおかしいと弾く.
        """
        print('賭ける金額を入力してください. (最低額 : '+ str(minimumBet) +')')
        while True:
            try:
                bet = int(input())
            except ValueError: #int型以外を入力された場合.
                print('\u001b[2A\u001b[0J', end='')
                print('int型で入力してください. (最低額 : '+ str(minimumBet) +')')
                continue
            if minimumBet > bet:
                print('\u001b[2A\u001b[0J', end='')
                print('最低額以上を賭けてください. (最低額 : '+ str(minimumBet) +')')
            elif bet > self.money:
                print('\u001b[2A\u001b[0J', end='')
                print('所持金を超過しています. (最低額 : '+ str(minimumBet) +')')
            else:
                break
        return bet

    def assign_bet(self, bet):
        """
        賭け金を代入する関数.
        """
        self.bet = bet
        self.betRate = self.bet/self.money
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
        print('あなたのモード : '+ str(self.mode))
        print('あなたの予想 : '+ coin.conversion(self.predict) +' ', end='')
        choices = ['Call', 'Fold']
        if self.predict == c_num: #プレイヤーの予想とコインが一致してるかの判定
            print('予想が的中しました.')
        else:
            print('予想が外れました.')
        print('コールしますか?', end='')
        print_choices(choices)
        call = select(choices)-1 #入力
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

    def input_doubt(self, players):
        """
        ダウトする相手を選択する関数.
        """
        choices = []
        for p in players:
            choices.append(p.name)
        choices.append('n')
        print('どのプレイヤーをダウトしますか？', end='')
        print_choices(choices)
        ans = select(choices) #入力
        doubt = None
        if ans == len(choices):
            print('ダウトしません.')
        else:
            doubt = players[ans-1]
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
        """
        doubt = self.doubt
        doubt.predict -= doubt.bluff #doubt.predictを本来の結果に戻す.
        print('\n'+ doubt.name +'が賭けた面は'+ coin.conversion(doubt.predict)+'でした.')

        if doubt.bluff == 1: #ダウト成功.
            steal = doubt.bet
            if doubt.mode == 'トリプルアップ': #奪う額が2倍になる.
                steal *= 2
            self.money += steal
            doubt.money -= steal

            print(self.name +'のダウトは成功です.')
            print(str(steal) +'円が'+ doubt.name +'から'+ self.name +'へ移動します.')

        else: #ダウト失敗.
            print(self.name +'のダウトは失敗です.')
            if doubt.mode == 'カウンター':
                doubt.counterAttack(self)

    def counterAttack(self, doubter):
        """
        カウンターを実行する関数.
        """
        steal = self.bet + self.counter
        self.money += steal
        doubter.money -= steal
        self.counter = 0
        print('カウンターにより'+ str(steal) +'円が'+ doubter.name +'から'+ self.name +'へ移動します.')

    def updateValue(self):
        """
        各プレイヤーの持っている値をリセットする.
        カウンターは更新する.
        """
        if self.isCall == False:
            if self.mode == 'カウンター': #カウンターでフォールドした場合,カウンターの値が保持される.
                self.counter += self.bet
            else:
                self.counter = self.bet
        else:
            decrease = int(self.counter/4) #ラウンド毎に4分の1減少.
            self.counter -= decrease
        self.mode = None
        self.predict = 0
        self.bet = 0
        self.isCall = False
        self.bluff = 0
        self.doubt = None

    def yourTurn(self):
        print(str(self.name) +'さんのターンです.')
        main.pleaseEnter(1)

def select(choices):
    """
    標準入力で選択肢を選ぶ関数.

    引数 :
        choices : 選択肢のリスト.str型.

    返り値 :
        ans : 選択した選択肢の番号が返る.
    """
    limmit = len(choices)
    while True:
        try:
            ans = int(input())
        except ValueError: #int型以外を入力された場合.
            print('\u001b[2A\u001b[0J', end='')
            print('int型で入力してください.', end='')
            print_choices(choices)
            continue
        if 0 < ans and ans <= limmit:
            break
        else: #選択肢から外れた数字を入力した場合.
            print('\u001b[2A\u001b[0J', end='')
            print('選択肢からお選びください.', end='')
            print_choices(choices)
    return ans

def print_choices(choices):
    """
    標準入力系の関数で選択肢をプリントする関数.
    選択文(1:5%, 2:10%, 3:15%, 4:20%, 5:30%)
    """
    print('(', end='')
    for n in range(len(choices)):
        print(str(n+1) +':', end='') #選択番号の表示.
        print(str(choices[n]), end='') #選択内容の表示.
        if n != len(choices)-1: #nがchoicesの最終要素でない時.
            print(', ', end='')
    print(')')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
