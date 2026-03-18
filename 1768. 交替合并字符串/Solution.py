class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        res = []
        l = r = 0
        while l < n1 or r < n2:
            if l < n1:
                res.append(word1[l])
                l += 1
            if r < n2:
                res.append(word2[r])
                r += 1
        return ''.join(res)