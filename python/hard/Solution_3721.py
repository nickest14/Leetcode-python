# 3721. Longest Balanced Subarray II

from typing import List


class SegmentTree:
    """Range add, then find leftmost index in [0, R] with value 0."""

    def __init__(self, n: int) -> None:
        self.n = n
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.min_val: list[int] = [0] * (2 * self.size)
        self.max_val: list[int] = [0] * (2 * self.size)
        self.lazy: list[int] = [0] * (2 * self.size)

    def _apply(self, i: int, d: int) -> None:
        self.min_val[i] += d
        self.max_val[i] += d
        if i < self.size:
            self.lazy[i] += d

    def _push(self, i: int) -> None:
        if self.lazy[i]:
            self._apply(2 * i, self.lazy[i])
            self._apply(2 * i + 1, self.lazy[i])
            self.lazy[i] = 0

    def update(self, left: int, right: int, d: int) -> None:
        """Add d to all indices in [left, right] (inclusive)."""
        left += self.size
        right += self.size
        L0, R0 = left, right
        while left <= right:
            if left % 2 == 1:
                self._apply(left, d)
                left += 1
            if right % 2 == 0:
                self._apply(right, d)
                right -= 1
            left //= 2
            right //= 2
        # pull: recompute min/max for ancestors (effective value = min(children) + own lazy)
        for node in [L0, R0]:
            while node > 1:
                node //= 2
                self.min_val[node] = min(
                    self.min_val[2 * node], self.min_val[2 * node + 1]
                )
                self.max_val[node] = max(
                    self.max_val[2 * node], self.max_val[2 * node + 1]
                )
                self.min_val[node] += self.lazy[node]
                self.max_val[node] += self.lazy[node]

    def _leftmost_zero(self, i: int, seg_lo: int, seg_hi: int, limit_r: int) -> int:
        """Find leftmost index in [seg_lo, min(seg_hi, limit_r)] with value 0. Return -1 if none."""
        if seg_lo > limit_r:
            return -1
        if i >= self.size:
            # leaf
            if self.min_val[i] == 0:
                return seg_lo
            return -1
        self._push(i)
        mid = (seg_lo + seg_hi) // 2
        has_zero_left = self.min_val[2 * i] <= 0 <= self.max_val[2 * i]
        if has_zero_left and seg_lo <= limit_r:
            left_res = self._leftmost_zero(2 * i, seg_lo, mid, limit_r)
            if left_res != -1:
                return left_res
        if mid + 1 <= limit_r:
            return self._leftmost_zero(2 * i + 1, mid + 1, seg_hi, limit_r)
        return -1

    def leftmost_zero(self, limit_r: int) -> int:
        """Leftmost index in [0, limit_r] with value 0. Return -1 if none."""
        if self.min_val[1] > 0 or self.max_val[1] < 0:
            return -1
        return self._leftmost_zero(1, 0, self.size - 1, limit_r)


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # balance[s] = (distinct_even - distinct_odd) for segment [s, j]
        # even contributes -1, odd contributes +1 → we want balance 0
        st = SegmentTree(n + 1)
        prev: dict[int, int] = {}
        ans = 0
        for j in range(n):
            v = nums[j]
            delta = -1 if (v % 2 == 0) else 1
            p = prev.get(v, -1)
            st.update(p + 1, j, delta)
            prev[v] = j
            i = st.leftmost_zero(j)
            if i != -1:
                ans = max(ans, j - i + 1)
        return ans
