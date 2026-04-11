# https://www.luogu.com.cn/problem/P1914

import sys

input = sys.stdin.readline

def main():
    n = int(input())
    s = input().strip()
    res = []
    for c in s:
        res.append(chr((ord(c) - ord('a') + n) % 26 + ord('a')))
    print(''.join(res))

if __name__ == '__main__':
    main()
