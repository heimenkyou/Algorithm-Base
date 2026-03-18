from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        cnt = 0
        for i in range(length):
            # 当前和两边都每种（或两边是边界），就立刻种植
            if (flowerbed[i] == 0 and 
                (i == 0 or flowerbed[i - 1] == 0) and 
                (i == length - 1 or flowerbed[i + 1] == 0)):
                cnt += 1
                flowerbed[i] = 1
        return cnt >= n