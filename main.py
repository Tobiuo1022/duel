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

        betPhase(players)

        declarer = d.checkDuel(players) #宣言者を決定.
        if declarer != None: #デュエルを宣言したプレイヤーがいればデュエルフェイズを行う.
            print('\n-- DuelPhase --') #デュエルフェイズ
            duelPhase(c, d, declarer, players)
            goNextRound = False
            continue

        d.announce_bet(players) #各プレイヤーの賭け金を公表.
        pleaseEnter(1)

        print('\n-- CoinToss --') #コイントス
        c.toss()
        pleaseEnter(1)

        callPhase(c, players)
        d.announce_call(c, players)

        doubtPhase(players)
        d.delete_overlap_doubt(players)

        d.announce_mode(players)
        pleaseEnter(1)
        print('')
        d.announce_doubt(players)
        pleaseEnter(1)

        detectPhase(players)

        payPhase(c, d, players)

        for p in players:
            p.updateValue()

    d.finishGame(players)

def betPhase(players):
    print('\n-- BetPhase --')
    for p in players:
        p.yourTurn()
        p.assign_mode(p.input_mode())
        if p.mode == 3: #デュエルモード
            others = players[:]
            others.remove(p)
            p.inputTarget(others)
        else:
            p.assign_predict(p.input_predict())
            p.assign_bet(p.input_bet())
            p.print_bet()
            pleaseEnter(9)

def callPhase(c, players):
    print('\n-- Call or Fold --')
    for p in players:
        p.yourTurn()
        p.assign_call(c.num, p.input_call(c.num))
        pleaseEnter(4)

def doubtPhase(players):
    print('\n-- DoubtPhase --')
    for p in players:
        p.yourTurn()
        others = players[:]
        others.remove(p)
        p.assign_doubt(p.input_doubt(others))
        pleaseEnter(5)

def detectPhase(players):
    for p in players:
        if linkId(p.doubt, players) != None:
            p.detect(players)
            pleaseEnter(1)

def payPhase(c, d, players):
    print('\n-- PayPhase --') #ペイフェイズ
    for p in players:
        d.pay(c, p)
    pleaseEnter(1)

def duelPhase(c, d, declarer, players):
    d.resetValue(players) #各プレイヤーのベッドを無かったことにする.
    declarer.duel(c, players)

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
