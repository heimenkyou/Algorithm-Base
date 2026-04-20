# https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        cnt = 0
        vowels = set('aeiou')
        for r, c in enumerate(s):
            if c in vowels:
                cnt += 1
            if r < k - 1:
                continue
            res = max(res, cnt)
            if s[r - k + 1] in vowels:
                cnt -= 1
        return res
