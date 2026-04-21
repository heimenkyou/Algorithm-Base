# https://leetcode.cn/problems/unique-number-of-occurrences/

from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 计数
        cnt = Counter(arr)
        # 值变成集合，看看数量有没有变少
        return len(cnt) == len(set(cnt.values()))
