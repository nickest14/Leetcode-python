# 698. Partition to K Equal Sum Subsets


from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        nums.sort(reverse=True)
        target = total / k
        visited = set()

        def backtrack(ind, count, curr_sum):
            if count == k:
                return True
            if target == curr_sum:
                return backtrack(0, count + 1, 0)

            for i in range(ind, len(nums)):
                if i > 0 and (i - 1) not in visited and nums[i] == nums[i - 1]:
                    continue
                if i in visited or curr_sum + nums[i] > target:
                    continue
                visited.add(i)

                if backtrack(i + 1, count, curr_sum + nums[i]):
                    return True
                visited.remove(i)

            return False

        return backtrack(0, 0, 0)


nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
ans = Solution().canPartitionKSubsets(nums, k)
print(ans)
