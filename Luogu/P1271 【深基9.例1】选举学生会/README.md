# P1271 【深基9.例1】选举学生会

[题目链接](https://www.luogu.com.cn/problem/P1271)

---

## 解题思路

Python 提供了两种排序方式，一种是**实例方法**（原地修改），另一种是**内置函数**（返回新对象，类似静态方法）。

---

### 1. 实例方法：`list.sort()`

* **对标 Java**：类似于 Java 8 引入的 `list.sort(Comparator)`。
* **特点**：**原地排序 (In-place)**。它直接修改原列表，不返回任何值（返回 `None`）。
* **注意**：如果你写 `a = list.sort()`，变量 `a` 会变成 `None`，这是新手最常犯的错。

```python
nums = [3, 1, 2]
nums.sort()  # 原地修改，没有返回值
print(nums)  # [1, 2, 3]
```

### 2. 内置函数：`sorted()`
这类似于 Java 的静态方法 `Collections.sort()`，但行为更像 Stream 流的 `.sorted()`。

* **对标 Java**：类似于 `list.stream().sorted().collect(Collectors.toList())`。
* **特点**：**返回新列表**。原列表保持不变。
* **优势**：它可以接收**任何可迭代对象**（字符串、集合、元组、字典的键），而不仅仅是列表。

```python
nums = [3, 1, 2]
new_nums = sorted(nums)  # 原列表 nums 不动，返回一个新列表
print(nums)      # [3, 1, 2]
print(new_nums)  # [1, 2, 3]

# 甚至可以排字符串
print(sorted("python")) # ['h', 'n', 'o', 'p', 't', 'y']
```

---

### 3. 考场深度对比



| 特性 | `list.sort()` (实例方法) | `sorted()` (内置函数) |
| :--- | :--- | :--- |
| **调用方式** | `mylist.sort()` | `sorted(mylist)` |
| **返回值** | `None` | **新的**已排序列表 |
| **原数据** | 被修改 | 不受影响 |
| **适用对象** | 仅限 `list` | 任意 Iterable (Set, Map, String等) |
| **性能** | 略快（不需要额外内存复制） | 略慢（需要开辟新空间） |

---

### 4. 关于自定义排序（Java 的 Comparator）
在 Python 中，无论用哪种方式，自定义逻辑都通过 `key` 参数实现。

* **Java**: `list.sort((a, b) -> a.score - b.score)`
* **Python**: `list.sort(key=lambda x: x.score)`

**特别提醒：**
Python 的排序默认只有升序。如果你要降序，不需要像 Java 那样写复杂的 `Collections.reverseOrder()`，只需要加一个参数：
`nums.sort(reverse=True)`

### 5. IDLE 救命指令
如果在赛场上记不清到底是 `sort(mylist)` 还是 `sorted(mylist)`，直接在 IDLE 交互界面输入：
1. `dir(list)`：会发现里面有 `sort`，说明它是列表的方法。
2. `dir(__builtins__)`：你会发现里面有 `sorted`，说明它是全局直接调用的函数。
