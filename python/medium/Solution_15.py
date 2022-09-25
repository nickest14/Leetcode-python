# 15. 3Sum


class Solution:
    def threeSum(self, nums):
        ans = []
        if len(nums) < 3:
            return ans
        data = {}
        nums.sort()
        new_nums = []
        for i in nums:
            if i in data.keys():
                if (i == 0 and data[i] > 2) or (i != 0 and data[i] > 1):
                    continue
                data[i] += 1
                new_nums.append(i)
            else:
                data[i] = 1
                new_nums.append(i)
        length = len(new_nums)
        for i in range(length-1):
            for j in range(i+1, length):
                data1 = new_nums[i]
                data2 = new_nums[j]
                data3 = 0 - data1 - data2
                if data3 in data.keys():
                    if data3 == data1 and data3 == data2:
                        if not data[data3] > 2:
                            continue
                    if data3 == data1 or data3 == data2:
                        if not data[data3] > 1:
                            continue
                    if data1 == data2:
                        if not data[data1] > 1:
                            continue
                    solution = [data1, data2, data3]
                    solution.sort()
                    if str(solution) in data.keys():
                        continue
                    else:
                        ans.append(solution)
                        data[str(solution)] = True
        return ans


# ans = Solution().threeSum([-1, 1, -1, -1, -1, -1, 2, 5, 0, 2, 2, 2, 6])
ans = Solution().threeSum([1, 1, 1])
# ans = Solution().threeSum([0, 0, 0, 0, 0, 0, 0, -1])

# ans = Solution().threeSum([-1, 0, 1, 2, -1, -4])
print(ans)
