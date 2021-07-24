# 155. Min Stack


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack and self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
