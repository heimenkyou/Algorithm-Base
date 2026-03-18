[238. 除了自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/)

---

**关于代码中的“前缀数组“和”后缀数组“：**

**不要把 `prefix[i]` 看作是 `nums[i]` 的前缀，而要把 `prefix[i]` 定义为“`nums[i]` 左边所有人的乘积”。**

这种错位是为了**把 `nums[i]` 给“空出来”**。

为了算“除了自己以外的乘积”，你必须在乘前缀时避开自己，乘后缀时也避开自己。

- **`prefix[i]`**：存储 `nums[0]` 到 `nums[i-1]` 的乘积（也就是 $i$ **左边**的所有人）。
- **`suffix[i]`**：存储 `nums[i+1]` 到 `nums[n-1]` 的乘积（也就是 $i$ **右边**的所有人）。