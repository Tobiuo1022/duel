import main, coin

class Dealer:

    def announce_state(self, players):
        print('各プレイヤーの所持金です.')
        for p in players:
            print(str(p.name) +'さん : 所持金 '+ str(p.money))

    def announce_bet(self, players):
        print('各プレイヤーの賭け金を公表します.')
        for p in players:
            print(str(p.name) +'さん : '+ str(p.bet) +' (所持金 '+ str(p.money) +')')

    def announce_call(self, coin, players):
        for p in players:
            if p.predict == coin.num:
                print(p.name +'さん : Call')
            else:
                print(p.name +'さん : Fold')

    def announce_doubt(self, players):
        print('ダウトの結果を公表します.')
        print('Please Enter', end='')
        hitEnter = input()
        print('\u001b[1A\u001b[0J', end='')

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
            print(doubted.name +'が賭けた面は'+ coin.conversion(doubted.predict)+'でした.')
            if doubted.bluff == 1:
                doubted.money -= doubted.bet;
                doubter.money += doubted.bet;
                print(doubter.name +'のダウトは成功です.'+ str(doubted.bet) +'円が'+ doubted.name +'から'+ doubter.name +'へ移動します.')
            else:
                doubter.money -= int(doubted.bet/2)
                print(doubter.name +'のダウトは失敗です.ペナルティとして'+ str(int(doubted.bet/2)) +'円を没収します.')
            print('Please Enter', end='')
            hitEnter = input()
            print('\u001b[1A\u001b[0J', end='')

    def pay(self, coin, player):
        """
        お金を清算する関数
        """
        if player.predict == coin.num:
            player.money += player.bet*2;
            print(player.name +'へ'+ str(player.bet*2) +'円をお支払いします.')
        else:
            print('残念ですが'+ player.name +'の賭金は没収となります.')
        player.bet = 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
