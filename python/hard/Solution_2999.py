# 2999. Count the Number of Powerful Integers


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        finish_length: int = len(str(finish))
        count_array: list[int] = [0] * (finish_length + 1)

        def count(n: str, target_str: str) -> int:
            result, index, size_diff = (
                count_array[len(n) - 1],
                0,
                len(n) - len(target_str),
            )
            while True:
                result += (
                    n[index:] >= target_str
                    if index == size_diff
                    else count_array[len(n) - index - 1]
                    * (min(limit, int(n[index]) - 1) + (index > 0))
                )
                index += 1
                if index > size_diff or int(n[index - 1]) > limit:
                    break
            return result

        for i in range(len(s), finish_length):
            count_array[i] = 1 if i == len(s) else count_array[i - 1] * (limit + 1)
        a = count(str(finish), s)
        b = count(str(finish), s)
        print(a, b)
        return count(str(finish), s) - count(str(start - 1), s)


# ans = Solution().numberOfPowerfulInt(1, 6000, 4, "124")
# ans = Solution().numberOfPowerfulInt(11, 3999, 4, "10")
ans = Solution().numberOfPowerfulInt(7, 50, 5, "8")
print(ans)


# n = 4
# edges = [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]]
# source = 0
# destination = 2
# target = 6
# ans = Solution().modifiedGraphEdges(n, edges, source, destination, target)
# print(ans)
