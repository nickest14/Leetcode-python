# 88. Merge Sorted Array


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_index = 0
        length = len(nums1)
        for _ in range(length-m):
            nums1.pop()
        for i in range(n):
            while num1_index < length:
                try:
                    if nums1[num1_index] >= nums2[i]:
                        nums1.insert(num1_index, nums2[i])
                        break
                except:
                    nums1.append(nums2[i])
                    break
                num1_index += 1
        print(nums1)


# Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
Solution().merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3)
