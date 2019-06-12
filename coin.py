'''
>>> import coin
>>> c = coin.Coin()
>>> print(c.face)
表
>>> print(c.num)
0
>>> c.conversion(1)
'裏'
>>> c.conversion(3)
'裏'
>>> c.conversion(0)
'表'
>>> c.conversion(2)
'表'
>>> c.toss()
>>> print(c.face)
表
>>> print(c.num)
0
'''

import random, time

class Coin:
    """
    コインのクラス.
    ディーラーがコイントスする際に使うコインと,
    プレイヤーがコイントスの結果を予想するときに使うコインの両方で使う.
    """
    face = '表' #表裏を示す.
    num = 0 #表裏を示す.偶数は表,奇数は裏に対応している.

    def __init__(self):
        self.num = 0
        self.face = conversion(self.num)

    def toss(self):
        """
        コイントスをする関数.
        """
        print('コイントス中…')
        time.sleep(2)
        print('\u001b[1A\u001b[0J', end='')
        self.num = random.randint(0, 1) #0か1の値を取る.
        self.face = conversion(self.num)
        print(self.face +'が出ました.')

def conversion(num):
    """
    numを引数にとって表裏で返す.変換器.
    """
    face = None
    if num % 2 == 0:
        face = '表' #偶数なら表.
    else:
        face = '裏' #奇数なら表.
    return face

if __name__ == '__main__':
    import doctest
    doctest.testmod()
