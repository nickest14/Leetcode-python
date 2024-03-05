# 380. Insert Delete GetRandom O(1)

from random import choice


class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        idx, last_element = self.dict[val], self.list[-1]
        self.list[idx], self.dict[last_element] = last_element, idx
        self.list.pop()
        del self.dict[val]

        return True

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
# param_1 = obj.insert(1)
# param_2 = obj.remove(1)
# param_3 = obj.insert(2)
# param_4 = obj.insert(3)
# param_5 = obj.getRandom()
# param_6 = obj.remove(2)
# print(f'{param_1} {param_2} {param_3} {param_4} {param_5} {param_6}')

param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.insert(2)
param_4 = obj.getRandom()
param_5 = obj.remove(1)
param_6 = obj.insert(2)
param_7 = obj.getRandom()
print(f'{param_1} {param_2} {param_3} {param_4} {param_5} {param_6} {param_7}')
