# https://leetcode.cn/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        l, r = 0, n - 1
        # 从两头往中间的双指针
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            res = max(res, h * w)
            # 谁低谁动，因为高的再往中间靠拢只会让结果更小
            if l < r and height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res