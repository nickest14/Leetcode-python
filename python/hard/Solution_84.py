# 84. Largest Rectangle in Histogram

class Solution:
    def largestRectangleArea(self, heights) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(i)
        return ans

# Slow
class Solution2:
    def __init__(self):
        self.area = 0

    def calculatearea(self, q, i, heights):
        for index in range(len(q)): 
            self.area = max(self.area, (i - q[index]['index'] + 1) * min(q[index]['height'], heights[i]))

    def prune(self, q, i, heights):
        index = 0
        seen = set()
        while index < len(q)-1:
            if heights[i] <= q[index]['height']:
                if heights[i] in seen:
                    q.pop(index)
                    index -= 1
                else:
                    seen.add(heights[i])
                    q[index]['height'] = heights[i]
            index += 1            

    def largestRectangleArea(self, heights) -> int:
        q = list()
        max_height = 0
        heights.append(0)
        length = len(heights)
        for i in range(length):
            if heights[i] <= 0:
                if i > 0:
                    i -= 1
                self.calculatearea(q, i, heights)
                q.clear()
            else:
                q.append({'index': i , 'height': heights[i]})

            if heights[i] < max_height:
                if i > 0:
                    self.calculatearea(q, i-1, heights)
                self.calculatearea(q, i, heights)
                self.prune(q, i, heights)
            max_height = heights[i]  
        return self.area
# li = [2,1,5,6,2,3]
li = [1,2,3,4,5]
li = [3,3,3,3,3]
ans = Solution().largestRectangleArea(li)
print(ans)
