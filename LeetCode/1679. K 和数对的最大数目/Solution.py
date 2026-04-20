# https://leetcode.cn/problems/max-number-of-k-sum-pairs/

from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = Counter(nums)
        for num in nums:
            if (k - num == num and cnt[num] >= 2) or (
                k - num != num and cnt[num] >= 1 and cnt[k - num] >= 1
            ):
                cnt[num] -= 1
                cnt[k - num] -= 1
                res += 1
        return res
