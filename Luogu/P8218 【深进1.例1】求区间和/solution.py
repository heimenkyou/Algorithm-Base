# https://www.luogu.com.cn/problem/P8218

import sys

input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]
    result = []
    for _ in range(m):
        l, r = map(int, input().split())
        result.append(prefix[r] - prefix[l - 1])
    sys.stdout.write('\n'.join(map(str, result)))

if __name__ == '__main__':
    main()
