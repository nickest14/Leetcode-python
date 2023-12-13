# 71. Simplify Path


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split("/"):
            # if i in ["/", "//"], it becomes ""
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == "":
                continue
            else:
                stack.append(i)
        return "/" + "/".join(stack)


ans = Solution().simplifyPath("/usr/home/../app/")
print(ans)
