# https://leetcode.cn/problems/find-the-highest-altitude/

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        height = 0
        for d in gain:
            height += d
            res = max(res, height)
        return res
