# https://www.luogu.com.cn/problem/P1097

import sys
from collections import Counter

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

def main():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    cnt = Counter(nums)
    for k in sorted(cnt):
        print(k, cnt[k])
        

if __name__ == '__main__':
    main()
