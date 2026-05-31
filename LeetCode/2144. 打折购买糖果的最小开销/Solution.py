# https://leetcode.cn/problems/minimum-cost-of-buying-candies-with-discount/


from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        sum_cost = 0
        cost.sort(reverse=True)
        for i, x in enumerate(cost):
            if i % 3 != 2:
                sum_cost += x
        return sum_cost
