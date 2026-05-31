# https://leetcode.cn/problems/find-pivot-index/

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumv = sum(nums)
        cur = 0
        for i, num in enumerate(nums):
            if cur + cur + num == sumv:
                return i
            cur += num
        return -1
