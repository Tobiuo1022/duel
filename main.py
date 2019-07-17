def play(d, players):
    print('\nゲームを開始します.')
    dealPhase(dc, players)
    pleaseEnter(1)
    round = 0
    while d.checkFinish(players) == False: #ゲームが終了するかの判定.

        higher = d.return_higher(players)
        lower = d.return_lower(players)
        if d.checkDuel(higher, lower) == True: #デュエルが行われるかの判定.
            print('')
            d.announce_jp(jp) #ジャックポットの金額を公表.
            print('')
            d.announce_state(players) #各プレイヤーの所持金を公表.
            pleaseEnter(1)

            duelPhase(c, jp, higher, lower) #デュエルフェイズ.
            if d.checkFinish(players) == True: #higherが勝てばゲーム終了.
                break
            d.announce_jp(jp) #ジャックポットの金額を公表.
            print('')
            d.announce_state(players) #各プレイヤーの所持金を公表.
            pleaseEnter(1)
            jackpotTime(jp, d, players) #ジャックポットタイム.
            continue

        round += 1
        print('\n-- '+ str(round) +'Round --') #ラウンド数.

        d.announce_jp(jp) #ジャックポットの金額を公表.
        print('')
        d.announce_state(players) #各プレイヤーの所持金を公表.
        pleaseEnter(1)

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

        detectPhase(jp, players) #ディテクトフェイズ.

        payPhase(c, jp, d, players) #ペイフェイズ.

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
        pleaseEnter(5)

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

def detectPhase(jp, players):
    for p in players:
        if p.doubt != None:
            p.detect(jp)
            pleaseEnter(1)

def payPhase(c, jp, d, players):
    print('\n-- PayPhase --')
    for p in players:
        d.pay(c, jp, p)
    pleaseEnter(1)

def duelPhase(c, jp, higher, lower):
    print('\n-- DuelPhase --')
    print(higher.name +'さんが'+ lower.name +'さんへデュエルを行います.')

    print(higher.name +'さん.')
    pleaseEnter(1)
    c.toss()
    success = higher.duel(c, jp) #攻撃側のコイントス.
    pleaseEnter(1)
    print('')

    if success == True:
        print(lower.name +'さん.')
        pleaseEnter(1)
        c.toss()
        lower.defense(c, jp, higher) #防衛側のコイントス.
        pleaseEnter(1)
        print('')

def jackpotTime(jp, d, players):
    print('\n-- JackPotTime --')
    d.announce_jp(jp)
    for p in players: #ジャックポットの配当の割合を決定.
        p.yourTurn()
        p.challenge(c)
    pleaseEnter(1)
    print('')

    jp.payJP(players) #ジャックポットの配当.
    pleaseEnter(1)

    for p in players:
        p.payRatio = 0

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
    import coin, jackpot, deck, dealer, player, sys
    c = coin.Coin()
    jp = jackpot.Jackpot()
    dc = deck.Deck()
    d = dealer.Dealer()
    players = []
    d.entry(players, d.entry_num())
    play(d, players)
    import doctest
    doctest.testmod()
