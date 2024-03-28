# 2405. Optimal Partition of String


class Solution:
    def partitionString(self, s: str) -> int:
        cur_set = set()
        ans = 0
        for c in s:
            if c in cur_set:
                print(cur_set)
                ans += 1
                cur_set = set()
            cur_set.add(c)

        ans += 1
        return ans


ans = Solution().partitionString("abacaba")
# ans = Solution().partitionString("ssssss")
print(ans)
