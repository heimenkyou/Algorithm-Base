# 443. 压缩字符串

[题目链接](https://leetcode.cn/problems/string-compression/)

---

解题思路：

**双指针**

- 快指针：找重复的，计数
- 慢指针：时刻指向应当被写入的位置

写入时机：找完一串重复元素后统一写入