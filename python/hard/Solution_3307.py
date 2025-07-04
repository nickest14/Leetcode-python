# 3307. Find the K-th Character in String Game II

from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        cnt: int = 0
        n: int = len(operations)
        length: int = pow(2, n - 1)
        for i in range(n - 1, -1, -1):
            if k > length:
                k -= length
                if operations[i] == 1:
                    cnt += 1
            length //= 2
        return chr(ord('a') + (cnt % 26))        


ans = Solution().kthCharacter(8, [1, 1, 1])
print(ans)
