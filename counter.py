class Counter(object):
    def __init__(self): #コンストラクタ
        self.cnt=0

    def doublecount(self):
        self.cnt += 2

    def reset(self):
        self.cnt = 0

    def show(self):
        print(self.cnt)

c = Counter()
c.show()
c.doublecount()
c.show()
