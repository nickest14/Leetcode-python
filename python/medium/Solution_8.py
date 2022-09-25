# 8. String to Integer (atoi)


class Solution:
    def myAtoi(self, str: str) -> int:
        ans = 0
        length = len(str)
        if length == 0:
            pass
        elif length == 1:
            ans = int(str) if str.isnumeric() else 0
        else:
            i = 0
            negative = False
            while i < length:
                if str[i] == ' ':
                    i += 1
                elif str[i] == '-':
                    negative = True
                    i += 1
                    break
                elif str[i] == '+':
                    i += 1
                    break
                else:
                    break

            while i < length:
                if str[i].isnumeric():
                    ans = ans * 10 + int(str[i])
                    i += 1
                else:
                    break
            if negative:
                ans *= -1
            if ans > 2**31 - 1:
                ans = 2**31 - 1
            elif ans < -2**31:
                ans = -2**31
        return ans

ans = Solution().myAtoi('  +998AAA656_J)(')
print(ans)
