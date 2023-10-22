# 901. Online Stock Span

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(100))  # return 1
print(obj.next(80))  # return 1
print(obj.next(60))  # return 1
print(obj.next(70))  # return 2
print(obj.next(60))  # return 1
print(obj.next(75))  # return 4
print(obj.next(85))  # return 6
