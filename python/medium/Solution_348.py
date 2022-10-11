# 348. Design Tic-Tac-Toe

import collections


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.counter = collections.Counter()
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        for i, c in enumerate([row, col, row + col, row - col]):
            self.counter[i, c, player] += 1
            if self.counter[i, c, player] == self.n:
                return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(3)
param_1 = obj.move(0, 0, 1)
param_2 = obj.move(0, 2, 2)
param_3 = obj.move(2, 2, 1)
param_4 = obj.move(1, 1, 2)
param_5 = obj.move(2, 0, 1)
param_6 = obj.move(1, 0, 2)
param_7 = obj.move(2, 1, 1)
