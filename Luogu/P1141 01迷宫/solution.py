# https://www.luogu.com.cn/problem/P1141

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)

def main():
    n, m = map(int, input().split())
    # 读取n行n列网格
    grid = [list(map(int, input().strip())) for _ in range(n)]
    result = [[0] * n for _ in range(n)]

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # 返回从x,y出发，剩下未到达但能到达的格子数量。同时记录访问路径坐标
    def dfs(x, y, path):
        # 标记已访问过并记录坐标
        result[x][y] = -1
        path.append((x, y))
        cnt = 1
        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            if (0 <= nx < n and 0 <= ny < n
                and result[nx][ny] == 0 and grid[nx][ny] != grid[x][y]):
                cnt += dfs(nx, ny, path)
        return cnt

    path = []
    for _ in range(m):
        i, j = map(int, input().split())
        i, j = i - 1, j - 1
        if result[i][j] != 0:
            print(result[i][j])
        else:
            path.clear()
            cnt = dfs(i, j, path)
            # 回填
            for x, y in path:
                result[x][y] = cnt
            print(cnt)

if __name__ == '__main__':
    main()
