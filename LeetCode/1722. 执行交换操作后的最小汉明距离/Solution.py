# https://leetcode.cn/problems/minimize-hamming-distance-after-swap-operations/

from collections import defaultdict
from typing import List


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        # 构造并查集
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in allowedSwaps:
            union(x, y)
        # 根据并查集分组，分成若干个联通分量
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        res = 0
        # 遍历每个连通分量，计算汉明距离
        for group in groups.values():
            cnt = defaultdict(int)
            diff = len(group)  # 不同元素的数量
            for index in group:
                cnt[source[index]] += 1
            # 在目标数组中，把存在于源数组的元素去掉
            for index in group:
                if cnt[target[index]] > 0:
                    diff -= 1
                    cnt[target[index]] -= 1
            res += diff
        return res
