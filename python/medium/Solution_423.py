# 423. Reconstruct Original Digits from English

import collections


class Solution:
    def originalDigits(self, s: str) -> str:
        counter = collections.Counter(s)
        print(counter)
        letters = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
        lookup = {'x': 6, 'u': 4, 'w': 2, 'z': 0, 'g': 8, 'o': 1, 'r': 3, 'f': 5, 'v': 7, 'n': 9}
        freq = [0] * 10
        for k, v in lookup.items():
            while k in counter:
                counter -= collections.Counter(letters[v])
                freq[v] += 1
        return ''.join(str(i) * count for i, count in enumerate(freq))


ans = Solution().originalDigits("owoztneoer")
# ans = Solution().originalDigits("zeroonetwothreefourfivesixseveneightnine")
print(ans)
