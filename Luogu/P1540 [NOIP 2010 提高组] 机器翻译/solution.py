# https://www.luogu.com.cn/problem/P1540

import sys
from collections import deque

input = sys.stdin.readline

def main():
    m, n = map(int, input().split())
    nums = list(map(int, input().split()))

    s = set()
    q = deque()
    cnt = 0
    for num in nums:
        if num in s:
            continue
        cnt += 1
        s.add(num)
        q.append(num)
        if len(q) > m:
            t = q.popleft()
            s.discard(t)
    print(cnt)

if __name__ == '__main__':
    main()
