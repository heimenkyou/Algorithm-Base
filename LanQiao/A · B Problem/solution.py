# https://www.lanqiao.cn/problems/20535/learning/

import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

def main():
    L = int(input())
    # cnt[i] 表示 i 的约数个数
    cnt = [0] * (L + 1)
    for i in range(1, L + 1):
        for j in range(i, L + 1, i):
            cnt[j] += 1
    # 计算前缀和
    prefix = [0] * (L + 1)
    for i in range(1, L + 1):
        prefix[i] = prefix[i - 1] + cnt[i]
    # 计算结果
    ans = 0
    for m in range(1, L):
        ans += cnt[m] * prefix[L - m]
    print(ans)
    

if __name__ == '__main__':
    main()
