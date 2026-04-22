# https://leetcode.cn/problems/equal-row-and-column-pairs/

from collections import Counter
from typing import List


# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         n = len(grid)

#         def is_same(i, j):
#             for k in range(n):
#                 if grid[i][k] != grid[k][j]:
#                     return False
#             return True

#         res = 0
#         for i in range(n):
#             for j in range(n):
#                 if is_same(i, j):
#                     res += 1
#         return res


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        cnt = Counter(tuple(row) for row in grid)
        for col in zip(*grid):
            res += cnt[tuple(col)]
        return res
