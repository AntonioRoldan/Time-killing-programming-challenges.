import random

class array():
    def __init__(self, summ, length):
        self.numbers_list = []
        self.sum = summ
        for i in range(length):
            self.numbers_list.append(random.randrange(1, 10))
    def numbers_adder(self):
        for x in self.numbers_list:
            self.formula = self.sum - x
            if self.formula in self.numbers_list and self.numbers_list.index(self.formula) != self.numbers_list.index(x) or x == self.sum//2:
                return (x, self.formula, True)
        return False
    def getnumberslist(self):
        print(self.numbers_list)


numbers_list = array(8, 8)
print(numbers_list.numbers_adder())
numbers_list.getnumberslist()

