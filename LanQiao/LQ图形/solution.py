# https://www.lanqiao.cn/problems/20563/learning/

import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

def main():
    w, h, v = map(int, input().split())
    # 画上半部分
    for _ in range(h):
        print('Q' * w)
    # 下半部分
    for _ in range(w):
        print('Q' * (v + w))

if __name__ == '__main__':
    main()
