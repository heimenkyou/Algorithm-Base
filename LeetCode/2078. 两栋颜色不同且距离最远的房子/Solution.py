# https://leetcode.cn/problems/two-furthest-houses-with-different-colors/

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        first, last = colors[0], colors[-1]
        # 首尾不相等直接输出
        if first != last:
            return len(colors) - 1
        res = 0
        # 找到某个不一样的点和首尾距离的最大值
        for i, color in enumerate(colors):
            if color != first:
                res = max(res, i)
            if color != last:
                res = max(res, len(colors) - i - 1)
        return res
