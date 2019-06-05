"""
>>> import dealer, player, coin
>>> c = coin.Coin()
>>> d = dealer.Dealer()
>>> p1 = player.Player(1)
>>> p2 = player.Player(2)
>>> p3 = player.Player(3)
>>> p4 = player.Player(4)

>>> print('ゲームを開始します.')
ゲームを開始します.
>>> p1.test_betting(0, 1000)
>>> p2.test_betting(0, 2000)
>>> p3.test_betting(1, 3000)
>>> p4.test_betting(1, 4000)

>>> print(p1.predict, p1.bet, p1.money)
0 1000 9000
>>> print(p2.predict, p2.bet, p2.money)
0 2000 8000
>>> print(p3.predict, p3.bet, p3.money)
1 3000 7000
>>> print(p4.predict, p4.bet, p4.money)
1 4000 6000

>>> d.announce_bet(p1, p2, p3, p4)
各プレイヤーの賭け金を公表します.
1さん : 1000 (所持金 9000)
2さん : 2000 (所持金 8000)
3さん : 3000 (所持金 7000)
4さん : 4000 (所持金 6000)

>>> c.num = 1
>>> c.face = coin.conversion(c.num)
>>> print(c.face +'が出ました.')
裏が出ました.

>>> p1.test_callOrFold(c, 0)
>>> p2.test_callOrFold(c, 1)
>>> p3.test_callOrFold(c, 2)
>>> p4.test_callOrFold(c, 1)
>>>
>>>
>>>
>>>
>>>
>>>
"""

def play(d, p1, p2, p3, p4):
    print('ゲームを開始します.')
    print('-- BetPhase --') #賭けフェイズ
    betPhase(p1, p2, p3, p4)
    d.announce_bet(p1, p2, p3, p4) #各プレイヤーの賭け金を公表.
    print('-- CoinToss --')
    c.toss()
    print(c.face +'が出ました.')
    print('-- Call or Fold --') #コールフェイズ
    callPhase(c, p1, p2, p3, p4)

def betPhase(p1, p2, p3, p4):
    p1.betting()
    p2.betting()
    p3.betting()
    p4.betting()

def callPhase(c, p1, p2, p3, p4):
    p1.callOrFold(c)
    p2.callOrFold(c)
    p3.callOrFold(c)
    p4.callOrFold(c)

if __name__ == '__main__':
    import dealer, player, coin
    c = coin.Coin()
    d = dealer.Dealer()
    p1 = player.Player(1)
    p2 = player.Player(2)
    p3 = player.Player(3)
    p4 = player.Player(4)
    play(d, p1, p2, p3, p4)
    import doctest
    doctest.testmod()
