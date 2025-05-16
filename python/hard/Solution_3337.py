# 3337. Total Characters in String After Transformations II

from typing import List


class Solution:
    def __init__(self):
        self.MOD: int = 10**9 + 7

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        T = self.getTransformationMatrix(nums)
        powered_T = self.matrixPow(T, t)

        count: list[int] = [0] * 26
        lengths: list[int] = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for i in range(26):
            for j in range(26):
                lengths[j] = (lengths[j] + count[i] * powered_T[i][j]) % self.MOD

        return sum(lengths) % self.MOD

    def getTransformationMatrix(self, nums: List[int]) -> List[List[int]]:
        T = [[0] * 26 for _ in range(26)]
        for i in range(len(nums)):
            for step in range(1, nums[i] + 1):
                T[i][(i + step) % 26] += 1
        return T

    def getIdentityMatrix(self, size: int) -> List[List[int]]:
        identity: List[List[int]] = [[0] * size for _ in range(size)]
        for i in range(size):
            identity[i][i] = 1
        return identity

    def matrixMult(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        size: int = len(A)
        C: List[List[int]] = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % self.MOD
        return C

    def matrixPow(self, M: List[int], n: int):
        if n == 0:
            return self.getIdentityMatrix(len(M))
        if n % 2 == 1:
            return self.matrixMult(M, self.matrixPow(M, n - 1))

        half = self.matrixPow(M, n // 2)
        return self.matrixMult(half, half)


ans = Solution().lengthAfterTransformations(
    "abcyy",
    2,
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
)
print(ans)
