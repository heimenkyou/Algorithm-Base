# https://www.luogu.com.cn/problem/P1271

import sys

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    for num in nums:
        print(num, end=' ')

if __name__ == '__main__':
    main()
