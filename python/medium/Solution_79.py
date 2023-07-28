# 79. Word Search

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (min(r, c) < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path):
                return False
            path.add((r, c))
            ans = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return ans

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


class Solution2:
    def exist(self, board, word: str) -> bool:
        if not word:
            return False
        self.board = board
        self.x_axis = len(board)
        self.y_axis = len(board[0])
        for x in range(self.x_axis):
            for y in range(self.y_axis):
                if board[x][y] == word[0]:
                    used = set()
                    used.add((x, y))
                    if self.checkword(x, y, word[1:], used):
                        return True
        return False

    def checkword(self, x, y, word, used):
        if len(word) == 0:
            return True
        # check up
        if x-1 >= 0 and (x-1, y) not in used and self.board[x-1][y] == word[0]:
            used.add((x-1, y))
            if self.checkword(x-1, y, word[1:], used):
                return True
            else:
                used.remove((x-1, y))            
        # check right
        if y+1 < self.y_axis  and (x, y+1) not in used and self.board[x][y+1] == word[0]:
            used.add((x, y+1))
            if self.checkword(x, y+1, word[1:], used):
                return True
            else:
                used.remove((x, y+1))
        # check down
        if x+1 < self.x_axis and (x+1, y) not in used and self.board[x+1][y] == word[0]:
            used.add((x+1, y))
            if self.checkword(x+1, y, word[1:], used):
                return True 
            else:
                used.remove((x+1, y))                   
        # check left
        if y-1 >= 0  and (x, y-1) not in used and self.board[x][y-1] == word[0]:
            used.add((x, y-1))
            if self.checkword(x, y-1, word[1:], used):
                return True  
            else:
                used.remove((x, y-1))
        return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = 'ASD'
ans = Solution().exist(board, word)
print(ans)
