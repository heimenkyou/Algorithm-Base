# https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/


from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt0 = 0
        res = 0
        l = 0
        for r, num in enumerate(nums):
            # 扩展右边界
            if num == 0:
                cnt0 += 1
            while cnt0 > 1 and l <= r:
                # 收缩左边界
                if nums[l] == 0:
                    cnt0 -= 1
                l += 1
            # 此时一定可以满足条件，记录结果
            res = max(res, r - l)  # (r - l + 1) - 1，区间长度 - 被删掉的一个元素
        return res
