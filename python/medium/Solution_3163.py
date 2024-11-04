# 3163. String Compression III


class Solution:
    def compressedString(self, word: str) -> str:
        ans: str = ''
        count: int = 1
        cur_c: str = word[0]
        for c in word[1:]:
            if c == cur_c and count < 9:
                count += 1
            else:
                ans += str(count) + cur_c
                count = 1
                cur_c = c
        ans += str(count) + cur_c
        return ans


ans = Solution().compressedString('aaaaaaaaaaaaaabb')
print(ans)
