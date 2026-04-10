# https://www.luogu.com.cn/problem/P3916

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    result = [0] * (n + 1)

    # 从cur开始遍历，将所有访问过的节点标记为val
    def dfs(cur, val):
        result[cur] = val
        for neighbor in g[cur]:
            if result[neighbor] == 0:
                dfs(neighbor, val)
    
    for _ in range(m):
        u, v = map(int, input().split())
        # 反向建边
        g[v].append(u)

    # 从大到小遍历所有点
    for i in range(n, 0, -1):
        if result[i] == 0:
            dfs(i, i)
    print(*result[1:])

if __name__ == '__main__':
    main()
