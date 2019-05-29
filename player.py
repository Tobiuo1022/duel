import coin
import dealer

class Player:
    playerNo = 0 #プレイヤーの番号.
    name = '' #プレイヤーの名前
    money = 10000 #所持金.
    counter = 0 #カウンターの値
    bet = 0 #賭け金
    # predict = 0 #予想した面.
    coin = coin.Coin()
    bluff = 0 #通常は偶数,嘘をつくと奇数が入る.
    douted = 0 #ダウト先のプレイヤー.

    def betting(self):
        """
        コイントスの結果を予想して所持金を賭ける関数.
        """
        print('どちらに賭けますか？(表, 裏)')
        self.coin.num = self.answer('表', '裏') #入力
        self.coin.face = self.coin.conversion(self.coin.num)
        print('いくら賭けますか？')
        self.bet = self.inputInt() #入力
        self.money -= self.bet
        print(self.coin.face, self.bet) #出力確認用

    def CallOrFold(self, dealer):
        """
        コイントスの結果と予想を判定して、降りるか降りないかを決める関数.
        """
        if self.coin.num == dealer.coin.num: #プレイヤーとディーラーのコインが一致してるかの判定
            print('予想が的中しました.(降りる, 降りない)')
            self.bluff = self.answer('降りる', '降りない') + 1
        else:
            print('予想が外れました.(降りる, 降りない)')
            self.bluff = self.answer('降りる', '降りない')
        print(self.bluff) #出力確認用

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
                print(zero + 'もしくは' + first + 'でお答えください.')
        return ans

    def inputInt(self):
        """
        int型を標準入力するための関数.
        """
        while True:
            try:
                ans = int(input())
            except ValueError: #int型以外を入力された場合.
                print('int型で入力してください.')
                continue
            if 0 < ans and ans <= self.money:
                break
            elif ans <= 0: #0以下を入力された場合.
                print('それでは賭けになりません.')
            else: #所持金を超えた額を入力された場合.
                print('賭け金が所持金を超えています.')
        return ans

if __name__ == '__main__':
    import doctest
    doctest.testmod()
