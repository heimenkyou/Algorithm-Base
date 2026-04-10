# https://www.luogu.com.cn/problem/P3378

import sys, heapq

input = sys.stdin.readline

def main():
    pq = []
    n = int(input())
    for _ in range(n):
        # 星号解包
        # args 会接收剩下的所有参数（变成一个列表），如果没有则为空
        op, *args = map(int, input().split())
        if op == 1:
            x = args[0]
            heapq.heappush(pq, x)
        elif op == 2:
            print(pq[0])
        else:
            heapq.heappop(pq)

if __name__ == '__main__':
    main()
