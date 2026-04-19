# 2078. 两栋颜色不同且距离最远的房子

[题目链接](https://leetcode.cn/problems/two-furthest-houses-with-different-colors/)

---

解题思路：

可以较为容易地推出来，这两个不一样的房子一定是从两端开始到中间某一点结束的

**反证：**

假设有不在两端的 l, r 为距离最大不同颜色房子，则两端至少有一端（start/end）与 (l, r) 颜色不同，则答案可以直接推到 [l, end] 或 [start, r]，假设不成立

**结论：**直接找距离两端点最远的不同颜色的点即可