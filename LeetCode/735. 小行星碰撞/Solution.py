# https://leetcode.cn/problems/asteroid-collision/


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for asteroid in asteroids:
            # 空的时候/不撞的时候放进去
            win = True
            # 如果会撞
            while win and len(res) > 0 and (res[-1] > 0 and asteroid < 0):
                win = res[-1] + asteroid < 0
                # 赢了或平局，都把对方弹出
                if res[-1] + asteroid <= 0:
                    res.pop()
                # 输了就自己拜拜
            if win:
                res.append(asteroid)
            # print(res[-1] if len(res) > 0 else None)
        return res
