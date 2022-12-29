# 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(num):
    ...


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (right + left) // 2
            result = guess(mid)
            match result:
                case -1:
                    right = mid - 1
                case 1:
                    left = mid + 1
                case 0:
                    return mid


ans = Solution().guessNumber(10)
print(ans)
