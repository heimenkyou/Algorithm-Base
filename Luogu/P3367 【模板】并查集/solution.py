# https://www.luogu.com.cn/problem/P3367

import sys

sys.setrecursionlimit(10**7)

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    res = []
    # 并查集
    parent = [i for i in range(n + 1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    for _ in range(m):
        z, x, y = map(int, input().split())
        if z == 1:
            union(x, y)
        else:
            res.append("Y" if find(x) == find(y) else "N")
    sys.stdout.write("\n".join(res))


if __name__ == "__main__":
    main()
