# 1346. Check If N and Its Double Exist

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        def binary_search(target: int) -> int:
            low, high = 0, len(arr) - 1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    low = mid + 1
                elif arr[mid] > target:
                    high = mid - 1

            return -1

        arr.sort()
        for i, val in enumerate(arr):
            index: int = binary_search(val * 2)
            if index != -1 and index != i:
                return True
        return False


ans = Solution().checkIfExist([10, 2, 5, 3])
print(ans)
