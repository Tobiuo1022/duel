def play(d, players):
    print('\nゲームを開始します.')
    dealPhase(dc, players)
    pleaseEnter(1)
    round = 0
    while d.checkFinish(players) == False: #ゲームが終了するかの判定.

        round += 1
        print('\n-- '+ str(round) +'Round --') #ラウンド数.

        print('')
        d.announce_state(players) #各プレイヤーの所持金を公表.
        pleaseEnter(1)

        d.calcMinimum(players)

        betPhase(players, d.minimumBet) #ベットフェイズ
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

        if len(dc.cards) < len(players):
            dc.shuffle()

        for p in players:
            dc.deal_cards(p)

        for p in players:
            p.updateValue() #値の更新.

    d.finishGame(players) #ゲーム終了.

def dealPhase(dc, players):
    dc.shuffle()
    for p in players:
        for i in range(4):
            dc.deal_cards(p)

def betPhase(players, minimumBet):
    print('\n-- BetPhase --')
    for p in players:
        p.yourTurn()
        p.assign_mode(p.input_mode())
        p.assign_predict(p.input_predict())
        bet = 0
        if p.money <= minimumBet:
            bet = p.input_minimum(minimumBet)
        else:
            bet = p.input_bet(minimumBet)
        p.assign_bet(bet)
        p.print_bet()
        pleaseEnter(9)

def callPhase(c, players):
    print('\n-- Call or Fold --')
    for p in players:
        p.yourTurn()
        p.assign_call(c.num, p.input_call(c.num))
        pleaseEnter(6)

def doubtPhase(players):
    print('\n-- DoubtPhase --')
    for p in players:
        p.yourTurn()
        if p.mode == 'ダウト':
            others = players[:] #リストの複製.
            others.remove(p) #自分以外のプレイヤーのリスト.
            p.assign_doubt(p.input_doubt(others))
            pleaseEnter(5)
        else:
            print('ダウトモードでないため,このフェイズはパスとなります.')
            pleaseEnter(3)

def detectPhase(players):
    for p in players:
        if p.doubt != None:
            p.detect()
            pleaseEnter(1)

def payPhase(c, d, players):
    print('\n-- PayPhase --')
    for p in players:
        d.pay(c, p)
    pleaseEnter(1)

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
    import coin, deck, dealer, player, sys
    c = coin.Coin()
    dc = deck.Deck()
    d = dealer.Dealer()
    players = []
    d.entry(players, d.entry_num())
    play(d, players)
    import doctest
    doctest.testmod()
