# https://leetcode.cn/problems/move-zeroes/

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 指向非0数应当处于的位置指针，同时也是非0数量
        left = 0
        for i in range(n):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1        
        # 将后面的元素置为0
        for i in range(left, n):
            nums[i] = 0