# 69. Sqrt(x)


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x <= 3:
            return 1
        left = 0
        right = int(x/2)
        last_mid = right
        while(left <= right):
            mid = int((left + right)/2)
            if x / mid > mid:
                left = mid + 1
                last_mid = mid
            elif x / mid < mid:
                right = mid - 1
            else:
                return mid
        return last_mid


ans = Solution().mySqrt(50)
print(ans)
