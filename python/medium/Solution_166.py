# 166. Fraction to Recurring Decimal


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    
        if not numerator:
            return "0"

        result: list[str] = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        num: int = abs(numerator)
        den: int = abs(denominator)

        result.append(str(num // den))
        num %= den

        if not num:
            return "".join(result)

        result.append(".")
        seen: dict[int, int] = {}

        while num:
            if num in seen:
                result.insert(seen[num], "(")
                result.append(")")
                break
            seen[num] = len(result)
            num *= 10
            result.append(str(num // den))
            num %= den

        return "".join(result)
        
        

ans = Solution().fractionToDecimal(4, 333)
print(ans)
