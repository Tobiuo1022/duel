import main

class Dealer:

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
            doubted = main.linkNameId(doubter.doubt, p1, p2, p3, p4)
            if doubted != None:
                print(doubter.name +' → '+ doubted)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
