# https://www.lanqiao.cn/problems/20564/learning/

import sys
sys.setrecursionlimit(10**7)

def main():
    n = 2025
    cnt = 1
    while True:
        n -= 5
        n -= 15 if cnt % 2 == 1 else 2
        if cnt % 3 == 1:
            n -= 2
        elif cnt % 3 == 2:
            n -= 10
        else:
            n -= 7
        if n <= 0:
            break
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
