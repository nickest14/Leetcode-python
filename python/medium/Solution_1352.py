# 1352. Product of the Last K Numbers


class ProductOfNumbers:
    def __init__(self):
        self.li: list[int] = []
        self.prod: int = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.prod = 1
            self.li = []
        else:
            self.prod *= num
            self.li.append(self.prod)

    def getProduct(self, k: int) -> int:
        if len(self.li) < k:
            return 0
        elif len(self.li) == k:
            return self.li[-1]
        else:
            return self.li[-1] // self.li[-k - 1]


obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
