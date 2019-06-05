import coin

class Dealer:

    def announce_bet(self, p1, p2, p3, p4):
        print('各プレイヤーの賭け金を公表します.')
        print(str(p1.name) +'さん : '+ str(p1.bet) +' (所持金 '+ str(p1.money) +')')
        print(str(p2.name) +'さん : '+ str(p2.bet) +' (所持金 '+ str(p2.money) +')')
        print(str(p3.name) +'さん : '+ str(p3.bet) +' (所持金 '+ str(p3.money) +')')
        print(str(p4.name) +'さん : '+ str(p4.bet) +' (所持金 '+ str(p4.money) +')')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
