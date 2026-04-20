# https://leetcode.cn/problems/max-number-of-k-sum-pairs/

from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = defaultdict(int)
        for num in nums:
            if cnt[k - num] > 0:
                cnt[k - num] -= 1
                res += 1
            else:
                cnt[num] += 1
        return res
