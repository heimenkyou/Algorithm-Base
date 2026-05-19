# https://leetcode.cn/problems/minimum-common-value/


from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        r = set(nums1) & set(nums2)
        return min(r) if len(r) > 0 else -1
