import main, coin

class Dealer:

    def announce_state(self, p1, p2, p3, p4):
        print('各プレイヤーの所持金です.')
        print(str(p1.name) +'さん : 所持金 '+ str(p1.money))
        print(str(p2.name) +'さん : 所持金 '+ str(p2.money))
        print(str(p3.name) +'さん : 所持金 '+ str(p3.money))
        print(str(p4.name) +'さん : 所持金 '+ str(p4.money))


    def announce_bet(self, p1, p2, p3, p4):
        print('各プレイヤーの賭け金を公表します.')
        print(str(p1.name) +'さん : '+ str(p1.bet) +' (所持金 '+ str(p1.money) +')')
        print(str(p2.name) +'さん : '+ str(p2.bet) +' (所持金 '+ str(p2.money) +')')
        print(str(p3.name) +'さん : '+ str(p3.bet) +' (所持金 '+ str(p3.money) +')')
        print(str(p4.name) +'さん : '+ str(p4.bet) +' (所持金 '+ str(p4.money) +')')

    def announce_doubt(self, p1, p2, p3, p4):
        print('ダウトの結果を公表します.')
        player = [p1, p2, p3, p4]

        count = 0
        for doubter in player:
            count += doubter.doubt
        if count == 0: #count == 0 → 誰もダウトをしていない.
            print('ダウトしたプレイヤーはいませんでした.')

        for doubter in player:
            doubted = main.linkId(doubter.doubt, p1, p2, p3, p4)
            if doubted != None:
                print(doubter.name +' → '+ doubted.name)

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
                doubter.money -= doubted.bet/2
                print(doubter.name +'のダウトは失敗です.ペナルティとして'+ str(int(doubted.bet/2)) +'円を没収します.')

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
