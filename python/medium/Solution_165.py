# 165. Compare Version Numbers


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1: list[int] = list(map(int, version1.split(".")))
        v2: list[int] = list(map(int, version2.split(".")))
        for i in range(max(len(v1), len(v2))):
            v1_val = v1[i] if i < len(v1) else 0
            v2_val = v2[i] if i < len(v2) else 0
            if v1_val > v2_val:
                return 1
            elif v1_val < v2_val:
                return -1
        return 0


ans = Solution().compareVersion("1.2", "1.10")
print(ans)
