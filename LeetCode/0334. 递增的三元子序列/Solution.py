# https://leetcode.cn/problems/increasing-triplet-subsequence/

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        has_left = [False] * n
        min_num = nums[0]
        for i in range(1, n):
            if min_num < nums[i]:
                has_left[i] = True
            min_num = min(min_num, nums[i])
        max_num = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if max_num > nums[i] and has_left[i]:
                return True
            max_num = max(max_num, nums[i])
        return False