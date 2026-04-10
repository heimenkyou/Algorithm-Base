# https://www.luogu.com.cn/problem/P1104

import sys

input = sys.stdin.readline


def main():
    n = int(input())
    students = []
    for id in range(n):
        name, year, month, day = input().split()
        students.append((name, int(year), int(month), int(day), id))
    students.sort(key=lambda x: (x[1], x[2], x[3], -x[4]))
    for student in students:
        print(student[0])

if __name__ == "__main__":
    main()
