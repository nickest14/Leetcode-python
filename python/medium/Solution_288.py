# 288. Unique Word Abbreviation

from typing import List


class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.abbrs = {}
        for word in dictionary:
            key = word and (word[0], len(word), word[-1])
            if key not in self.abbrs:
                self.abbrs[key] = hash(word)
            elif self.abbrs[key] != hash(word):
                self.abbrs[key] = None

    def isUnique(self, word: str) -> bool:
        key = word and (word[0], len(word), word[-1])
        return key not in self.abbrs or self.abbrs[key] == hash(word)


# Your ValidWordAbbr object will be instantiated and called as such:
dictionary = ['deer', 'door', 'cake', 'card']
obj = ValidWordAbbr(dictionary)
print(obj.isUnique("dear"))
print(obj.isUnique("cart"))
print(obj.isUnique("cane"))
print(obj.isUnique("make"))
