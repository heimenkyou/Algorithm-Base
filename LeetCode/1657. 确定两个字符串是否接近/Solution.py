# https://leetcode.cn/problems/determine-if-two-strings-are-close/

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return cnt1.keys() == cnt2.keys() and sorted(cnt1.values()) == sorted(cnt2.values())
