"""
>>> import dealer, player, coin
>>> c = coin.Coin()
>>> d = dealer.Dealer()
>>> p1 = player.Player(1, '1さん')
>>> p2 = player.Player(2, '2さん')
>>> p3 = player.Player(3, '3さん')
>>> p4 = player.Player(4, '4さん')

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
1さんさん : 1000 (所持金 9000)
2さんさん : 2000 (所持金 8000)
3さんさん : 3000 (所持金 7000)
4さんさん : 4000 (所持金 6000)

>>> c.num = 1
>>> c.face = coin.conversion(c.num)
>>> print(c.face +'が出ました.')
裏が出ました.

>>> p1.test_callOrFold(c, 0)
>>> p2.test_callOrFold(c, 1)
>>> p3.test_callOrFold(c, 2)
>>> p4.test_callOrFold(c, 1)

>>> p1.doubt = 0
>>> p2.doubt = 1
>>> p3.doubt = 2
>>> p4.doubt = 3

>>> d.announce_doubt(p1, p2, p3, p4)
ダウトの結果を公表します.
2さん → 1さん
3さん → 2さん
4さん → 3さん

>>> detectPhase(p1, p2, p3, p4)

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
    print('-- DoubtPhase --') #ダウトフェイズ
    doubtPhase(p1, p2, p3, p4)
    d.annouce_doubt(p1, p2, p3, p4)

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

def doubtPhase(p1, p2, p3, p4):
    p1.inputDoubt(p2, p3, p4)
    p2.inputDoubt(p1, p3, p4)
    p3.inputDoubt(p1, p2, p4)
    p4.inputDoubt(p1, p2, p3)

def detectPhase(p1, p2, p3, p4):
    pass

def linkNameId(id, p1, p2, p3, p4):
    """
    プレイヤーのIDを引数に対応したプレイヤーのnameを返す関数.
    """
    name = None
    if id == 1:
        name = p1.name
    elif id == 2:
        name = p2.name
    elif id == 3:
        name = p3.name
    elif id == 4:
        name = p4.name
    else:
        name = None
    return name

if __name__ == '__main__':
    import dealer, player, coin
    c = coin.Coin()
    d = dealer.Dealer()
    p1 = player.Player(1, '1さん')
    p2 = player.Player(2, '2さん')
    p3 = player.Player(3, '3さん')
    p4 = player.Player(4, '4さん')
    play(d, p1, p2, p3, p4)
    import doctest
    doctest.testmod()
