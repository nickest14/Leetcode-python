# 504. Base 7

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num *= -1
            prefix = '-'
        else:
            prefix = ''

        ans = ''
        while num:
            num, r = divmod(num, 7)
            ans += str(r)

        return prefix + ans[::-1]


ans = Solution().convertToBase7(100)
print(ans)

# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
# For the left two athletes, you just need to output their relative ranks according to their scores.
