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
各プレイヤーの所持金とカウンターの値です.
1さんさん : [所持金 10000] [カウンター 0]
2さんさん : [所持金 10000] [カウンター 0]
3さんさん : [所持金 10000] [カウンター 0]
4さんさん : [所持金 10000] [カウンター 0]

>>> p1.mode = 0
>>> p2.mode = 1
>>> p3.mode = 0
>>> p4.mode = 2

>>> p2.counter = 50

>>> p1.test_betting(0, 100)
>>> p2.test_betting(0, 200)
>>> p3.test_betting(1, 300)
>>> p4.test_betting(1, 400)

>>> print(p1.predict, p1.bet, p1.money)
0 100 9900
>>> print(p2.predict, p2.bet, p2.money)
0 200 9800
>>> print(p3.predict, p3.bet, p3.money)
1 300 9700
>>> print(p4.predict, p4.bet, p4.money)
1 400 9600

>>> d.announce_bet(players)
各プレイヤーの賭けた内容を公表します.
1さんさん : [モード ダウト] [賭け金 100] [所持金 9900]
2さんさん : [モード カウンター] [賭け金 200] [所持金 9800]
3さんさん : [モード ダウト] [賭け金 300] [所持金 9700]
4さんさん : [モード ダブルアップ] [賭け金 400] [所持金 9600]

>>> c.num = 0
>>> c.face = coin.conversion(c.num)
>>> print(c.face +'が出ました.')
表が出ました.

>>> p1.test_callOrFold(c, 1)
>>> p2.test_callOrFold(c, 1)
>>> p3.test_callOrFold(c, 0)
>>> p4.test_callOrFold(c, 1)

>>> d.announce_call(c, players)
1さんさん : Call
2さんさん : Call
3さんさん : Fold
4さんさん : Call

>>> p1.doubt = 2
>>> p2.doubt = 0
>>> p3.doubt = 0
>>> p4.doubt = 0

>>> d.test_announce_doubt(players)
ダウトの結果を公表します.
1さん → 2さん

>>> d.test_detect(p1, p2)
<BLANKLINE>
2さんが賭けた面は表でした.
1さんのダウトは失敗です.ペナルティとして150円を没収します.

>>> print(p1.money)
9750
>>> print(p2.money)
9800
>>> print(p3.money)
9700
>>> print(p4.money)
9600

>>> payPhase(c, d, players)
1さんへ200円をお支払いします.
2さんへ400円をお支払いします.
残念ですが3さんの賭金は没収となります.
4さんへ1200円をお支払いします.

>>> updateValue(players)

>>> print(p1.mode, p1.bet, p1.predict, p1.bluff, p1.call, p1.doubt, p4.target)
0 0 0 0 0 0 0
>>> print(p2.mode, p2.bet, p2.predict, p2.bluff, p2.call, p2.doubt, p4.target)
0 0 0 0 0 0 0
>>> print(p3.mode, p3.bet, p3.predict, p3.bluff, p3.call, p3.doubt, p4.target)
0 0 0 0 0 0 0
>>> print(p4.mode, p4.bet, p4.predict, p4.bluff, p4.call, p4.doubt, p4.target)
0 0 0 0 0 0 0

>>> print(p1.money, p1.counter)
9950 0
>>> print(p2.money, p2.counter)
10200 25
>>> print(int(p3.money), p3.counter)
9700 150
>>> print(p4.money, p4.counter)
10800 0

>>> p1.money = 0
>>> d.checkFinish(players)
True

>>> d.finishGame(players)
<BLANKLINE>
-- FinishGame --
各プレイヤーの所持金とカウンターの値です.
1さんさん : [所持金 0] [カウンター 0]
2さんさん : [所持金 10200] [カウンター 25]
3さんさん : [所持金 9700] [カウンター 150]
4さんさん : [所持金 10800] [カウンター 0]
<BLANKLINE>
1さんさんの所持金が無くなりました.
4さんさんの勝利です!

>>> p1.money = 10000
>>> p2.money = 10000
>>> p3.money = 10000
>>> p4.money = 10000

>>> p1.counter = 0
>>> p2.counter = 0
>>> p3.counter = 0
>>> p4.counter = 0

>>> p1.mode = 3
>>> p2.mode = 1
>>> p3.mode = 3
>>> p4.mode = 2

>>> p1.target = 4
>>> p2.test_betting(0, 200)
>>> p3.target = 4
>>> p4.test_betting(1, 400)

>>> declarer = d.checkDuel(players)
>>> d.resetValue(players)
>>> print(p2.predict, p2.bet, p2.money)
0 0 10000
>>> print(p4.predict, p4.bet, p4.money)
0 0 10000
>>> declarer.test_duel(c, players, False)
>>> print(p1.predict, p1.money)
0 5000
>>> print(p4.money)
15000

>>>
>>>
>>>
>>>
"""

def play(d, players):
    d.entry(players)
    print('\nゲームを開始します.')
    round = 0
    goNextRound = True
    while d.checkFinish(players) == False:
        if goNextRound == True:
            round += 1
            print('\n-- '+ str(round) +'Round --')
        else:
            print('再度BetPhaseを行います.\n')
            goNextRound = True

        d.announce_state(players) #各プレイヤーの所持金を公表.

        print('\n-- BetPhase --') #賭けフェイズ
        betPhase(players)

        declarer = d.checkDuel(players) #宣言者を決定.
        if declarer != None: #デュエルを宣言したプレイヤーがいればデュエルフェイズを行う.
            print('\n-- DuelPhase --') #デュエルフェイズ
            duelPhase(c, d, declarer, players)
            goNextRound = False
            continue

        d.announce_bet(players) #各プレイヤーの賭け金を公表.

        print('\n-- CoinToss --') #コイントス
        c.toss()
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

        updateValue(players) #カウンター値の更新

    d.finishGame(players)

def betPhase(players):
    for p in players:
        p.selectMode()
        if p.mode == 3: #デュエルモード
            others = players[:]
            others.remove(p)
            p.inputTarget(others)
        else:
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

def duelPhase(c, d, declarer, players):
    d.resetValue(players) #各プレイヤーのベッドを無かったことにする.
    declarer.duel(c, players)

def updateValue(players):
    """
    各プレイヤーの持っている値をリセットする.
    カウンターは更新する.
    """
    for p in players:
        if p.mode == 1:
            p.counter = int(p.counter/2)
        if p.call == 0:
            p.counter = int(p.bet/2)
        p.mode = 0
        p.bet = 0
        p.predict = 0
        p.call = 0
        p.bluff = 0
        p.doubt = 0

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
