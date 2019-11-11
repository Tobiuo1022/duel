import random, player

class Bot(player.Player):

    def __init__(self, playerNo, name):
        super(Bot, self).__init__(playerNo, name)

    def input_mode(self):
        """
        モードをランダムに選択する関数.
        """
        print('モードを選択中…')
        print('………')
        choices = self.hands
        ans = random.randint(1, len(choices))
        mode = self.hands.pop(ans-1)
        return mode

    def print_mode(self):
        pass

    def input_predict(self):
        """
        コイントスの予想をランダムに選択する関数.
        """
        print('コインの予想を選択中…')
        print('………')
        predict = random.randint(0, 1)
        return predict

    def input_bet(self, minimumBet):
        """
        賭け金をランダムに選択する関数.
        """
        print('賭金を選択中…')
        print('………')
        print('………')
        wishRate = random.randint(10, 30) * 0.01
        wishBet = int(self.money * wishRate)
        if minimumBet <= wishBet:
            bet = wishBet
        else:
            bet = minimumBet

        return bet

    def print_bet(self):
        pass

    def input_call(self, c_num):
        """
        コイントスの結果と予想を判定して、コールかフォールドランダムに選択する関数.

        引数 :
            c_num : コインの表裏を示す.0は表,1は裏に対応している.

        返り値 :
            call : コールなら0,フォールドなら1が入る.
        """
        print('コールかフォールドかを選択中…')
        print('………')
        print('………')
        print('………')
        if self.predict == c_num:
            call = 0
        else:
            if self.mode == 'トリプルアップ':
                call = 0
            elif self.mode == 'ダウト':
                call = random.randint(0, 1)
            else:
                call = 1
        return call

    def print_dontDoubt(self):
        print('ダウト先を選択中…')

    def input_doubt(self, players):
        """
        ダウトする相手を選択する関数.
        """
        print('ダウト先を選択中…')
        print('………')
        print('………')
        choices = []
        for p in players:
            if p.isCall == True:
                choices.append(p)
        choices.append('n')
        ans = random.randint(1, len(choices))
        doubt = None
        if ans == len(choices):
            pass
        else:
            doubt = choices[ans-1]
        return doubt
