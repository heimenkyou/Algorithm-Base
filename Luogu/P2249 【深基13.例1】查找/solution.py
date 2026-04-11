# https://www.luogu.com.cn/problem/P2249

import sys
from bisect import bisect_left

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    result = []
    for target in map(int, input().split()):
        index = bisect_left(nums, target)
        if 0 <= index < n and nums[index] == target:
            result.append(index + 1)
        else:
            result.append(-1)
    # 统一输出
    sys.stdout.write(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
