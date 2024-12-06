# 2825. Make String a Subsequence Using Cyclic Increments

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str1_len, str2_len = len(str1), len(str2)
        target_char = str2[0]

        str1_idx = str2_idx = 0

        while str1_idx < str1_len and str2_idx < str2_len:
            str1_char = str1[str1_idx]
            if (
                str1_char == target_char or
                chr(ord(str1_char) + 1) == target_char or
                (str1_char == 'z' and target_char == 'a')
            ):
                str2_idx += 1
                if str2_idx < str2_len:
                    target_char = str2[str2_idx]
            str1_idx += 1

        return str2_idx == str2_len


ans = Solution().canMakeSubsequence('abc', 'ad')
# ans = Solution().canMakeSubsequence('adgy', 'aegz')
print(ans)
