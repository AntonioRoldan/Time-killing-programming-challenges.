import random

class array():
    def __init__(self, summ):
        self.numbers_list = []
        while True:
            if self.numbers_list != 0:
                self.numbers_list = [i for i in range(random.randrange(1, 10))]
                break
            else:
                continue
        self.c = 0
        self.sum = summ
        for n in self.numbers_list:
            self.random_modifier = self.c + random.randrange(1, len(self.numbers_list))
            try:
                self.numbers_list[self.c] = self.numbers_list[self.random_modifier]
            except:
                if self.numbers_list[self.c] > len(self.numbers_list):
                    self.adjustment_value = len(self.numbers_list) - self.random_modifier
                    self.random_modifier -= adjustment_value + random.randrange(1, adjustment_value)
            self.c += 1
    def numbers_adder(self):
        threshold = len(self.numbers_list)
        count = 0
        for x in self.numbers_list:
            self.formula = self.sum - x
            if self.formula in self.numbers_list and self.numbers_list.index(self.formula) != self.numbers_list.index(x) or x == self.sum//2:
                return (x, self.formula, True)
            count += 1
        return False
    def getnumberslist(self):
        print(self.numbers_list)


numbers_list = array(8)
print(numbers_list.numbers_adder())
numbers_list.getnumberslist()
