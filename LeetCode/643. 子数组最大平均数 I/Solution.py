# https://leetcode.cn/problems/maximum-average-subarray-i/

from cmath import inf
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        max_sum = -inf
        for r, num in enumerate(nums):
            sum += num
            if r < k - 1:
                continue
            max_sum = max(max_sum, sum)
            sum -= nums[r - k + 1]
        return max_sum / k
