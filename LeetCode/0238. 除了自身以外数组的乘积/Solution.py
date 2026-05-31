from typing import List


class Solution:
    """
    前缀数组：prefix[i] = nums[0] * ... * nums[i-1]
    后缀数组：suffix[i] = nums[i+1] * ... * nums[n-1]
    结果：result[i] = prefix[i] * suffix[i]
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        return [prefix[i] * suffix[i] for i in range(n)]
