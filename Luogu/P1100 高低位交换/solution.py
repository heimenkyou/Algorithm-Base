# https://www.luogu.com.cn/problem/P1100

import sys

input = sys.stdin.readline

def main():
    n = int(input())
    # 低位左移，高位右移
    res = ((n & 0x0000FFFF) << 16) | (n >> 16)
    print(res)

if __name__ == '__main__':
    main()
