# 353. Design Snake Game

from typing import List
import collections


class SnakeGame:
    mapping = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.foods = collections.deque(food)
        self.snake = collections.deque([(0, 0)])
        self.blocks = set([(0, 0)])

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = r, c = tuple(p + d for p, d in zip(self.snake[0], self.mapping[direction]))
        tail = self.snake.pop()
        self.blocks.discard(tail)
        if head in self.snake or not (0 <= r < self.height) or not (0 <= c < self.width):
            return -1
        self.snake.appendleft(head)
        self.blocks.add(head)
        if self.foods and head == tuple(self.foods[0]):
            self.foods.popleft()
            self.snake.append(tail)
            self.blocks.add(tail)
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
obj = SnakeGame(3, 5, [[1, 2], [0, 1]])
param_1 = obj.move('R')
param_2 = obj.move('D')
param_3 = obj.move('R')
param_4 = obj.move('U')
param_5 = obj.move('L')
param_6 = obj.move('U')
print(F'{param_1=} {param_2=} {param_3=} {param_4=} {param_5=} {param_6=}')
