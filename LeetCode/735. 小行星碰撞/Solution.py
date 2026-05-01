# https://leetcode.cn/problems/asteroid-collision/


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        res = []
        for asteroid in asteroids:
            # 空的时候/不撞的时候放进去
            if len(res) == 0 or not (res[-1] > 0 and asteroid < 0):
                res.append(asteroid)
            else:
                win = True
                # 如果会撞
                while len(res) > 0 and (res[-1] > 0 and asteroid < 0):
                    # 赢了
                    if res[-1] + asteroid < 0:
                        res.pop()
                    # 如果平局就同归于尽
                    elif res[-1] + asteroid == 0:
                        res.pop()
                        win = False
                        break
                    # 输了就拜拜
                    else:
                        win = False
                        break
                if win:
                    res.append(asteroid)
            # print(res[-1] if len(res) > 0 else None)
        return res
