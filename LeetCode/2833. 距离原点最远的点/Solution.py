# https://leetcode.cn/problems/furthest-point-from-origin/


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        pos = 0
        cnt = 0
        for move in moves:
            if move == 'L':
                pos -= 1
            elif move == 'R':
                pos += 1
            else:
                cnt += 1
        return abs(pos) + cnt
