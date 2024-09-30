# 1381. Design a Stack With Increment Operation


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack: list[int] = [0] * maxSize
        self.top: int = -1

    def push(self, x: int) -> None:
        if self.top < len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top != -1:
            value = self.stack[self.top]
            self.top -= 1
            return value
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.top + 1)):
            self.stack[i] += val


obj = CustomStack(3)
obj.push(1)
obj.push(2)
print(obj.pop())
obj.push(2)
obj.push(3)
obj.push(4)
obj.increment(5, 100)
obj.increment(2, 100)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
