# 3606. Coupon Code Validator

from typing import List


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        e_group: list[str] = []
        g_group: list[str] = []
        p_group: list[str] = []
        r_group: list[str] = []
        for i in range(len(code)):
            if not isActive[i]:
                continue
            bl = businessLine[i]
            if bl not in ("electronics", "grocery", "pharmacy", "restaurant"):
                continue

            if not code[i]:
                continue

            if not all(ch.isalnum() or ch == "_" for ch in code[i]):
                continue

            if bl.startswith("e"):
                e_group.append(code[i])
            if bl.startswith("g"):
                g_group.append(code[i])
            if bl.startswith("p"):
                p_group.append(code[i])
            if bl.startswith("r"):
                r_group.append(code[i])

        return sorted(e_group) + sorted(g_group) + sorted(p_group) + sorted(r_group)


code = ["SAVE20", "", "PHARMA5", "SAVE@20"]
businessLine = ["restaurant", "grocery", "pharmacy", "restaurant"]
isActive = [True, True, True, True]
ans = Solution().validateCoupons(code, businessLine, isActive)
print(ans)
