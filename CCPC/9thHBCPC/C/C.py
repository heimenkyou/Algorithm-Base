# https://codeforces.com/gym/105909

import sys

input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        # 每个样例
        n, m, k, x = map(int, input().split())
        vs = []  # 潜力值
        diff = 0  # 总分差
        for _ in range(n):
            b, c = map(int, input().split())
            vs.append(c - k * b)  # 只存潜力值
            diff -= b * c  # 提前扣除惩罚分，后面只计算增量收益
        # 按潜力值从大到小排序，分配分数
        vs.sort(reverse=True)
        for v in vs:
            if m <= 0:
                break
            # 分配分数，能给x分就给x分，不能就给剩余的m分
            a = min(m, x)
            m -= a
            # 计算分数差
            diff += k * a * a + v * a
        if m > 0: # 如果还有分数没分配完，说明无法满足条件
            print('NO')
        elif diff > 0:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
