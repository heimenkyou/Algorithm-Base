# https://codeforces.com/gym/105909
# Python被卡常了，Damn！

import sys

input = sys.stdin.readline


# 在排好序的数组里，差值小于等于 x 的对子，一共有多少个
def count_lt(x, a):
    cnt = 0
    l = 0
    for r, num in enumerate(a):
        while l < r and num - a[l] > x:
            l += 1
        if l < r and num - a[l] <= x:
            cnt += r - l
    return cnt


def main():
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:]))

    a.sort()
    l, r = 0, 10**8
    # 1. 通过二分找到第 k 大的差值 D
    D = r
    while l <= r:
        mid = (l + r) // 2
        if count_lt(mid, a) >= k:
            r = mid - 1
            D = mid
        else:
            l = mid + 1
    # 拿到D后，计算所有差值小于D的对子的和
    # 提前计算前缀和
    prefix = [0] * (n + 1)
    for i, num in enumerate(a):
        prefix[i + 1] = prefix[i] + num
    # 2. 双指针计算
    ans = 0
    cnt = 0
    l = 0
    for r in range(n):
        while l < r and a[r] - a[l] >= D:
            l += 1
        if l < r and a[r] - a[l] < D:
            cnt += r - l
            ans += (r - l) * a[r] - (prefix[r] - prefix[l])

    # 可能个数不够 k 个，直接拿等于 D 的补齐
    ans += (k - cnt) * D
    print(ans)


if __name__ == '__main__':
    main()
