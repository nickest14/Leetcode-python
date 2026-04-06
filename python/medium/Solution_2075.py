# 2075. Decode the Slanted Ciphertext


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        n: int = len(encodedText)
        cols: int = n // rows
        ans: list[str] = []

        for col in range(cols):
            row = 0
            while row < rows and col < cols:
                ans.append(encodedText[row * cols + col])
                row += 1
                col += 1

        return "".join(ans).rstrip()


ans = Solution().decodeCiphertext('ch   ie   pr', 3)
print(ans)
