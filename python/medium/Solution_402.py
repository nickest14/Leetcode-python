# 402. Remove K Digits


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)

        stack = stack[:len(stack) - k]
        ans = "".join(stack)
        return str(int(ans)) if ans else "0"


ans = Solution().removeKdigits("1432219", 3)
print(ans)
