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
>>> p3.test_callOrFold(c, 0)
>>> p4.test_callOrFold(c, 0)

>>> p1.doubt = 2
>>> p2.doubt = 0
>>> p3.doubt = 4
>>> p4.doubt = 0

>>> d.announce_doubt(p1, p2, p3, p4)
ダウトの結果を公表します.
1さん → 2さん
3さん → 4さん

>>> detectPhase(p1, p2, p3, p4)
2さんが賭けた面は表でした.
1さんのダウトは成功です.2000円が2さんから1さんへ移動します.
4さんが賭けた面は裏でした.
3さんのダウトは失敗です.ペナルティとして2000円を没収します.

>>> print(p1.money)
11000
>>> print(p2.money)
6000
>>> print(int(p3.money))
5000
>>> print(p4.money)
6000

>>>
>>>
>>>
>>>
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
    print('-- DoubtPhase --') #ダウトフェイズ
    doubtPhase(p1, p2, p3, p4)
    d.announce_doubt(p1, p2, p3, p4)
    detectPhase(p1, p2, p3, p4)

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
    p1.detect(linkId(p1.doubt, p1, p2, p3, p4))
    p2.detect(linkId(p2.doubt, p1, p2, p3, p4))
    p3.detect(linkId(p3.doubt, p1, p2, p3, p4))
    p4.detect(linkId(p4.doubt, p1, p2, p3, p4))

def linkId(id, p1, p2, p3, p4):
    """
    プレイヤーのIDを引数に対応したplayerを返す関数.
    """
    player = None
    if id == 1:
        player = p1
    elif id == 2:
        player = p2
    elif id == 3:
        player = p3
    elif id == 4:
        player = p4
    else:
        player = None
    return player

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
