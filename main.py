"""
>>> import dealer, player, coin
>>> c = coin.Coin()
>>> d = dealer.Dealer()
>>> p1 = player.Player(1, '1さん')
>>> p2 = player.Player(2, '2さん')
>>> p3 = player.Player(3, '3さん')
>>> p4 = player.Player(4, '4さん')
>>> players = [p1, p2, p3, p4]

>>> print('ゲームを開始します.')
ゲームを開始します.

>>> checkFinish(players)
False

>>> d.announce_state(players)
各プレイヤーの所持金です.
1さんさん : 所持金 10000
2さんさん : 所持金 10000
3さんさん : 所持金 10000
4さんさん : 所持金 10000

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

>>> d.announce_bet(players)
各プレイヤーの賭け金を公表します.
1さんさん : 1000 (所持金 9000)
2さんさん : 2000 (所持金 8000)
3さんさん : 3000 (所持金 7000)
4さんさん : 4000 (所持金 6000)

>>> c.num = 1
>>> c.face = coin.conversion(c.num)
>>> print(c.face +'が出ました.')
裏が出ました.

>>> p1.test_callOrFold(1)
>>> p2.test_callOrFold(1)
>>> p3.test_callOrFold(0)
>>> p4.test_callOrFold(0)

>>> p1.doubt = 2
>>> p2.doubt = 0
>>> p3.doubt = 4
>>> p4.doubt = 0

>>> d.announce_doubt(players)
ダウトの結果を公表します.
1さん → 2さん
3さん → 4さん

>>> detectPhase(d, players)
2さんが賭けた面は表でした.
1さんのダウトは成功です.2000円が2さんから1さんへ移動します.
4さんが賭けた面は裏でした.
3さんのダウトは失敗です.ペナルティとして2000円を没収します.

>>> print(p1.money)
11000
>>> print(p2.money)
6000
>>> print(p3.money)
5000
>>> print(p4.money)
6000

>>> payPhase(c, d, players)
1さんへ2000円をお支払いします.
残念ですが2さんの賭金は没収となります.
3さんへ6000円をお支払いします.
4さんへ8000円をお支払いします.

>>> print(p1.money, p1.bet)
13000 0
>>> print(p2.money, p1.bet)
6000 0
>>> print(int(p3.money), p1.bet)
11000 0
>>> print(p4.money, p1.bet)
14000 0

>>> p2.money = 0
>>> checkFinish(players)
2さんさんの所持金が無くなりました.
True

>>> finishGame(players)
4さんさんの勝利です!

>>>
>>>
>>>
>>>
>>>
>>>
"""

def play(d, players):
    print('ゲームを開始します.')
    while checkFinish(players) == False:
        d.announce_state(players) #各プレイヤーの所持金を公表.

        print('-- BetPhase --') #賭けフェイズ
        betPhase(players)
        d.announce_bet(players) #各プレイヤーの賭け金を公表.

        print('-- CoinToss --') #コイントス
        c.toss()
        print(c.face +'が出ました.')
        pleaseEnter(1)

        print('-- Call or Fold --') #コールフェイズ
        callPhase(c, players)
        d.announce_call(c, players)

        print('-- DoubtPhase --') #ダウトフェイズ
        doubtPhase(players)
        d.announce_doubt(players)
        detectPhase(d, players)

        print('-- PayPhase --') #ペイフェイズ
        payPhase(c, d, players)
        if checkFinish(players) == True:
            break
        print('-- NextTurn --')
    finishGame(players)

def betPhase(players):
    for p in players:
        p.betting()

def callPhase(c, players):
    for p in players:
        p.callOrFold(c)

def doubtPhase(players):
    for p in players:
        others = players[:]
        others.remove(p)
        p.inputDoubt(others)

def detectPhase(d, players):
    for p in players:
        d.detect(p, linkId(p.doubt, players))

def payPhase(c, d, players):
    for p in players:
        d.pay(c, p)

def linkId(id, players):
    """
    プレイヤーのIDを引数に対応したplayerを返す関数.
    """
    player = None
    for p in players:
        if id == p.playerNo:
            player = p

    return player

def checkFinish(players):
    """
    各プレイヤーの所持金が0になったか確認する関数.
    """
    finish = False
    for p in players:
        if p.money <= 0:
            finish = True
            print(p.name +'さんの所持金が無くなりました.')
    return finish

def finishGame(players):
    """
    最も所持金の多いプレイヤーを勝者とする関数.
    """
    winners = []
    maxim = 0
    for p in players:
        if p.money > maxim:
            winners.clear()
            winners.append(p)
            maxim = p.money
        elif p.money == maxim:
            winners.append(p)

    for winner in winners:
        print(winner.name +'さん', end='')
    print('の勝利です!')

def pleaseEnter(num):
        """
        Please Enterを出力し,引数numの値だけ出力された行を消す関数.

        引数 :
        num : 消す行数の数.
        """
        print('Please Enter', end='')
        hitEnter = input()
        print('\u001b[%dA\u001b[0J' % num, end='')

if __name__ == '__main__':
    import dealer, player, coin, sys
    c = coin.Coin()
    d = dealer.Dealer()
    p1 = player.Player(1, '1さん')
    p2 = player.Player(2, '2さん')
    p3 = player.Player(3, '3さん')
    p4 = player.Player(4, '4さん')
    players = [p1, p2, p3, p4]
    play(d, players)
    import doctest
    doctest.testmod()
