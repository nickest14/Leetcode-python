# 1106. Parsing A Boolean Expression

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for c in expression:
            if c != ')' and c != ',':
                stack.append(c)
            elif c == ')':
                exp = []

                while stack and stack[-1] != '(':
                    t = stack.pop()
                    exp.append(True if t == 't' else False)

                stack.pop()

                if stack:
                    t = stack.pop()
                    v = exp[0]
                    if t == '&':
                        for b in exp:
                            v &= b
                    elif t == '|':
                        for b in exp:
                            v |= b
                    else:
                        v = not v

                    stack.append('t' if v else 'f')

        return stack[-1] == 't'


ans = Solution().parseBoolExpr('|(f,f,f,t)')
# ans = Solution().parseBoolExpr('!(&(f,t))')
print(ans)
