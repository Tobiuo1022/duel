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

>>> d.checkFinish(players)
False

>>> d.announce_state(players)
各プレイヤーの所持金です.
1さんさん : 所持金 10000
2さんさん : 所持金 10000
3さんさん : 所持金 10000
4さんさん : 所持金 10000

>>> p1.mode = 0
>>> p2.mode = 0
>>> p3.mode = 0
>>> p4.mode = 2

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

>>> c.num = 0
>>> c.face = coin.conversion(c.num)
>>> print(c.face +'が出ました.')
表が出ました.

>>> p1.test_callOrFold(0)
>>> p2.test_callOrFold(0)
>>> p3.test_callOrFold(0)
>>> p4.test_callOrFold(1)

>>> d.announce_call(c, players)
1さんさん : Call
2さんさん : Call
3さんさん : Fold
4さんさん : Call

>>> p1.doubt = 2
>>> p2.doubt = 0
>>> p3.doubt = 4
>>> p4.doubt = 0

>>> d.test_announce_doubt(players)
ダウトの結果を公表します.
1さん → 2さん
3さん → 4さん

>>> d.test_detect(p1, p2)
<BLANKLINE>
2さんが賭けた面は表でした.
1さんのダウトは失敗です.ペナルティとして1000円を没収します.
>>> d.test_detect(p3, p4)
<BLANKLINE>
4さんが賭けた面は裏でした.
3さんのダウトは成功です.8000円が4さんから3さんへ移動します.

>>> print(p1.money)
8000
>>> print(p2.money)
8000
>>> print(p3.money)
15000
>>> print(p4.money)
-2000

>>> payPhase(c, d, players)
1さんへ2000円をお支払いします.
2さんへ4000円をお支払いします.
残念ですが3さんの賭金は没収となります.
残念ですが4さんの賭金は没収となります.

>>> print(p1.money, p1.bet)
10000 0
>>> print(p2.money, p1.bet)
12000 0
>>> print(int(p3.money), p1.bet)
15000 0
>>> print(p4.money, p1.bet)
-2000 0

>>> p1.money = 0
>>> d.checkFinish(players)
True

>>> d.finishGame(players)
<BLANKLINE>
-- FinishGame --
各プレイヤーの所持金です.
1さんさん : 所持金 0
2さんさん : 所持金 12000
3さんさん : 所持金 15000
4さんさん : 所持金 -2000
<BLANKLINE>
1さんさん4さんさんの所持金が無くなりました.
3さんさんの勝利です!


>>>
>>>
>>>
>>>
>>>
>>>
"""

def play(d, players):
    d.entry(players)
    print('\nゲームを開始します.')
    round = 0
    while d.checkFinish(players) == False:
        round += 1
        print('\n-- '+ str(round) +'Round --')
        d.announce_state(players) #各プレイヤーの所持金を公表.

        print('\n-- BetPhase --') #賭けフェイズ
        betPhase(players)
        d.announce_bet(players) #各プレイヤーの賭け金を公表.

        print('\n-- CoinToss --') #コイントス
        c.toss()
        print(c.face +'が出ました.')
        pleaseEnter(1)

        print('\n-- Call or Fold --') #コールフェイズ
        callPhase(c, players)
        d.announce_call(c, players)

        print('\n-- DoubtPhase --') #ダウトフェイズ
        doubtPhase(players)
        d.announce_doubt(players)
        detectPhase(d, players)

        print('\n-- PayPhase --') #ペイフェイズ
        payPhase(c, d, players)
        pleaseEnter(1)

    d.finishGame(players)

def betPhase(players):
    for p in players:
        p.selectMode()
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
    players = []
    play(d, players)
    import doctest
    doctest.testmod()
