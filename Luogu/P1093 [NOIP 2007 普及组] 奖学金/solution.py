# https://www.luogu.com.cn/problem/P1093

import sys

input = sys.stdin.readline


class Student:
    def __init__(self, id, cn, math, eng):
        self.id = id
        self.cn = cn
        self.math = math
        self.eng = eng
        self.score = cn + math + eng

    def __lt__(self, other):
        if self.score != other.score:
            return self.score > other.score
        if self.cn != other.cn:
            return self.cn > other.cn
        return self.id < other.id


def main():
    n = int(input())
    students = [None] * n
    for id in range(1, n + 1):
        cn, math, eng = map(int, input().split())
        students[id - 1] = Student(id, cn, math, eng)
    students.sort()
    for i in range(5):
        print(f"{students[i].id} {students[i].score}")


if __name__ == "__main__":
    main()
