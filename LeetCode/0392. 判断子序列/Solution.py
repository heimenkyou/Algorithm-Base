# https://leetcode.cn/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(t), len(s)
        index = 0
        for i in range(n):
            if index < m and t[i] == s[index]:
                index += 1
        return index == m
