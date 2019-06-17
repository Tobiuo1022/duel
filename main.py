def play(d, players):
    print('\nゲームを開始します.')
    pleaseEnter(1)
    round = 0
    nextRound = True #ペイフェイズとデュエルフェイズのどちらから戻ってきたのかの判定.
    while d.checkFinish(players) == False: #ゲームが終了するかの判定.
        if nextRound == True:
            round += 1
            print('\n-- '+ str(round) +'Round --') #ラウンド数.

        d.announce_state(players) #各プレイヤーの所持金を公表.
        pleaseEnter(1)

        higher = d.return_higher(players)
        lower = d.return_lower(players)
        if d.checkDuel(higher, lower) == True: #デュエルが行われるかの判定.
            duelPhase(c, higher, lower) #デュエルフェイズ.
            nextRound = False
            continue
        else:
            nextRound = True

        betPhase(players) #ベットフェイズ
        d.announce_bet(players) #各プレイヤーの賭け金を公表.
        pleaseEnter(1)

        print('\n-- CoinToss --') #コイントス
        c.toss()
        pleaseEnter(1)

        callPhase(c, players) #コールフェイズ.
        d.announce_call(c, players) #各プレイヤーのコールを公表.
        pleaseEnter(1)

        doubtPhase(players) #ダウトフェイズ.
        d.delete_overlap_doubt(players) #複数のプレイヤーで重複したダウトを消す.

        d.announce_mode(players) #各プレイヤーのモードを公表.
        pleaseEnter(1)
        print('')
        d.announce_doubt(players) #各プレイヤーのダウト先を公表.
        pleaseEnter(1)

        detectPhase(players) #ディテクトフェイズ.

        payPhase(c, d, players) #ペイフェイズ.

        for p in players:
            p.updateValue() #値の更新.

    d.finishGame(players) #ゲーム終了.

def betPhase(players):
    print('\n-- BetPhase --')
    for p in players:
        p.yourTurn()
        p.assign_mode(p.input_mode())
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
        others = players[:] #リストの複製.
        others.remove(p)
        p.assign_doubt(p.input_doubt(others))
        pleaseEnter(5)

def detectPhase(players):
    for p in players:
        if p.doubt != None:
            p.detect()
            pleaseEnter(1)

def payPhase(c, d, players):
    print('\n-- PayPhase --') #ペイフェイズ
    for p in players:
        d.pay(c, p)
    pleaseEnter(1)

def duelPhase(c, higher, lower):
    print('\n-- DuelPhase --') #デュエルフェイズ
    print(higher.name +'さんが'+ lower.name +'さんへデュエルを行います.')

    print(higher.name +'さん.')
    pleaseEnter(1)
    higher.assign_predict(higher.input_predict())

    c.toss()
    pleaseEnter(1)
    print('')

    higher.duel(c, lower)
    pleaseEnter(1)
    print('')

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
    d.entry(players, d.entry_num())
    play(d, players)
    import doctest
    doctest.testmod()
