# 28. Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        pre_fix = self.get_pre_fix(needle, needle_len)
        i, j = 0, 0
        while i < haystack_len and j < needle_len:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = pre_fix[j]
        if j < needle_len:
            return -1
        else:
            return i-needle_len

    def get_pre_fix(self, needle, needle_len):
        j = 0
        i = 1
        pre_fix = [0 for i in range(needle_len)]
        while i < needle_len:
            if needle[i] == needle[j]:
                pre_fix[i] = pre_fix[i-1] + 1
                j += 1
            elif needle[i] == needle[i-1] and pre_fix[i-1] > 0:
                pre_fix[i] = pre_fix[i-1]
            else:
                j = 0
            i += 1
        pre_fix.insert(0, -1)
        return pre_fix

    # Brute-force solution
    def strStr_2(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        if needle_len == 0:
            return 0
        if haystack_len == 0:
            return -1
        first_alpha = needle[0]
        for i in range(haystack_len):
            if haystack[i] == first_alpha:
                if haystack[i:i+needle_len] == needle:
                    return i
        return -1


haystack = 'abaacababcac'
needle = 'ababcdef'

haystack = "aabaaabaaac"
needle = "aabaaac"
ans = Solution().strStr(haystack, needle)
print(ans)
