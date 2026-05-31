# https://leetcode.cn/problems/string-compression/

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        index = 0
        i = 0
        while i < n:
            c = chars[i]
            cnt = 0
            while i < n and chars[i] == c:
                i += 1
                cnt += 1
            # 赋值第一个字符
            chars[index] = c
            index += 1
            # 填充数量数字
            if cnt == 1:
                continue
            cnt = str(cnt)
            for digit in cnt:
                chars[index] = digit
                index += 1
        return index
