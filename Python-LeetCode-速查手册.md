# Python 刷 LeetCode 常用工具函数速查手册

> 按**使用场景**分类整理，每个工具都给出「用法 + 典型题目场景 + 代码片段」。
> 需要时直接 Ctrl+F 搜关键字。

---

## 目录

- [一、字符串 str 常用方法](#一字符串-str-常用方法)
- [二、列表 list（栈 / 数组 / 双指针）](#二列表-list栈--数组--双指针)
- [三、排序 sorted / sort](#三排序-sorted--sort)
- [四、字典 dict / defaultdict / Counter](#四字典-dict--defaultdict--counter)
- [五、集合 set](#五集合-set)
- [六、deque 双端队列](#六deque-双端队列)
- [七、heapq 堆](#七heapq-堆)
- [八、bisect 二分查找](#八bisect-二分查找)
- [九、functools](#九functools)
- [十、itertools](#十itertools)
- [十一、数学 / 位运算 / 边界值](#十一数学--位运算--边界值)
- [十二、递归 / 输入板子](#十二递归--输入板子)
- [十三、高频一句话模板](#十三高频一句话模板)
- [十四、五个高频坑](#十四五个高频坑)
- [附录：按题型反查工具](#附录按题型反查工具)

---

## 一、字符串 str 常用方法

| 方法 | 用法 | 典型场景 |
|---|---|---|
| `c.isdigit()` | 判断是否为数字字符 `'0'~'9'` | 解析表达式（394 字符串解码、227 基本计算器） |
| `c.isalpha()` | 是否为字母 | 单词/字母统计，验证回文串 |
| `c.isalnum()` | 字母或数字 | 125 验证回文串（先过滤再判断） |
| `c.isupper() / islower()` | 大小写判断 | 大小写转换类题 |
| `c.upper() / lower()` | 转大小写 | 784 字母大小写全排列 |
| `s.split(sep)` | 按分隔符切分成 list | 单词拆分、路径解析 |
| `sep.join(list)` | list 拼成字符串 | **大量拼接必须用 `join`**，避免 `+=` 的 O(n²) |
| `s.strip()` | 去首尾空白 | 8. 字符串转整数 atoi |
| `s.find(sub) / index(sub)` | 找子串位置；`find` 找不到返回 -1，`index` 抛异常 | KMP 类题（手写更快，小数据可用内置） |
| `s.count(sub)` | 子串计数 | 单字符统计时 `Counter` 更通用 |
| `s.startswith(p) / endswith(p)` | 前缀/后缀判断 | 单词搜索、Trie 匹配 |
| `s.replace(a, b)` | 替换 | 简单文本处理 |
| `s[::-1]` | 反转字符串 | 回文判断 `if s == s[::-1]` |
| `ord(c) / chr(n)` | 字符 ↔ ASCII 码 | **字母哈希桶**，用于异位词、频次统计 |

```python
# 字母计数桶：异位词、字符频次统计（比 dict 更快）
cnt = [0] * 26
for c in s:
    cnt[ord(c) - ord('a')] += 1

# 回文判断
is_palindrome = (s == s[::-1])

# 过滤非字母数字后判断（125 题）
clean = ''.join(c.lower() for c in s if c.isalnum())
```

---

## 二、列表 list（栈 / 数组 / 双指针）

栈是 LeetCode 里最高频的结构：

```python
stack = []
stack.append(x)        # 入栈 O(1)
top = stack[-1]        # 看栈顶 O(1)
x = stack.pop()        # 出栈（尾部）O(1)
while stack and ...:   # 判空时先写 stack，防止 IndexError（394 题就是这个写法）
```

> ⚠️ **不要用 `list.pop(0)` 或 `insert(0, x)`**，它们都是 **O(n)**，数据一大就 TLE。
> 需要队首操作时用 `collections.deque`。

其他高频：

```python
a[i:j]              # 切片 O(j-i)，会产生拷贝
a[::-1]             # 反转
sorted(a)           # 返回新列表；a.sort() 原地排序
sum(a) / max(a) / min(a)
max(a, key=lambda x: x[1])          # 按自定义键取最大
any(...) / all(...)                 # 存在 / 全部满足
enumerate(a, start=1)               # 同时拿下标和值
zip(a, b)                           # 并行遍历
zip(*matrix)                        # 矩阵转置（48 旋转图像）
[0] * n                             # 一维初始化
[[0] * n for _ in range(m)]         # 二维初始化（绝不能写 [[0]*n]*m，行会共享引用！）
```

`enumerate` / `zip` 常见用法：

```python
for i, v in enumerate(nums): ...
for a, b in zip(nums[:-1], nums[1:]): ...        # 相邻元素对
for i in range(len(nums) - 1, -1, -1): ...       # 倒序遍历下标
```

---

## 三、排序 sorted / sort

```python
sorted(items, key=lambda x: x[1])           # 按第二维排序
sorted(items, key=lambda x: (x[0], -x[1]))  # 多关键字：第一升序，第二降序
sorted(s)                                   # 字符串排序 → 字符列表
''.join(sorted(s))                          # 排序后拼回，可作异位词签名
nums.sort(key=lambda x: (len(x), x))        # 自定义优先级
```

要点：

- `sorted` 返回新列表，`list.sort()` **原地修改**（无返回值）
- Python 排序是**稳定排序**（相等元素保持原相对顺序）
- 降序用 `reverse=True`；数字多关键字降序可用取负 `-x[1]` 的技巧
- 需要复杂比较器时用 `functools.cmp_to_key`（如「把数组排成最小的数」）

```python
from functools import cmp_to_key
# 179. 最大数：a+b 与 b+a 比较
nums.sort(key=cmp_to_key(lambda a, b: int(a + b) - int(b + a)))
```

---

## 四、字典 dict / defaultdict / Counter

```python
d = {}
d.get(k, 0)                     # 安全取值，键不存在返回默认值
d[k] = d.get(k, 0) + 1          # 手写计数
d.setdefault(k, []).append(v)   # 建图邻接表，省去判空
d.pop(k, default)
for k, v in d.items(): ...
```

### collections 三件套（强烈建议默认导入）

```python
from collections import defaultdict, Counter, deque

graph = defaultdict(list)   # 邻接表：graph[u].append(v) 不用判空
freq  = defaultdict(int)    # 计数：freq[x] += 1
seen  = defaultdict(set)

cnt = Counter(s)                    # 一行统计频次
cnt.most_common(k)                  # 出现次数前 k 个 → 347 前 K 个高频元素
Counter("abc") == Counter("bca")    # True，判断异位词
cnt1 - cnt2                         # 计数相减（76 最小覆盖子串常用）
cnt1 & cnt2                         # 取交集（每个键取较小计数）
```

> ⚠️ 遍历字典时**不能增删键**，需要快照：`for k in list(d.keys())`。

---

## 五、集合 set

```python
seen = set()
seen.add(x)
seen.discard(x)     # 不存在也不报错（remove 会抛 KeyError）
if x in seen: ...   # O(1) 查找

a | b   # 并集
a & b   # 交集  → 349 两个数组的交集
a - b   # 差集
a ^ b   # 对称差（只出现一次的元素）
frozenset(...)  # 可作为 dict 的键 / 放進 set
```

场景：两数之和查补数、去重、环形链表（节点 id 入集合）、岛屿问题的 visited。

```python
# 1. 两数之和
seen = set()
for x in nums:
    if target - x in seen:
        return True
    seen.add(x)
```

---

## 六、deque 双端队列

```python
from collections import deque

q = deque([root])
q.append(x); q.popleft()        # 队列：两端都 O(1)
q.appendleft(x); q.pop()        # 反向操作
q = deque(maxlen=3)             # 固定长度，满了自动丢弃另一端
len(q)                          # O(1)
```

场景：**BFS 层序遍历**、二叉树层序、滑动窗口最大值（单调队列）。

```python
# 二叉树层序遍历（102）
q = deque([root])
while q:
    node = q.popleft()
    if node.left:  q.append(node.left)
    if node.right: q.append(node.right)
```

---

## 七、heapq 堆

Python 只有**小顶堆**，要大顶堆就存负数。

```python
import heapq

h = []
heapq.heappush(h, x)
smallest = heapq.heappop(h)
h[0]                        # 只看堆顶，不弹出 O(1)
heapq.heapify(list)         # 原地建堆 O(n)

# 大顶堆：存负数
heapq.heappush(h, -x)
biggest = -heapq.heappop(h)

# 按优先级排序：元组比较，先比第一项
heapq.heappush(h, (dist, node))     # Dijkstra
heapq.heappush(h, (freq, word))     # 注意第二项也要可比较

heapq.nlargest(k, arr)      # 前 k 大
heapq.nsmallest(k, arr)     # 前 k 小
```

场景：215 第K大、347 前K高频、23 合并K个有序链表、973 最接近原点的K个点、
295 数据流中位数（大顶堆 + 小顶堆对半分）。

```python
# TopK 经典写法：维护大小为 k 的小顶堆
for x in nums:
    heapq.heappush(h, x)
    if len(h) > k:
        heapq.heappop(h)
return h[0]     # 堆顶即第 k 大
```

---

## 八、bisect 二分查找

```python
import bisect

i = bisect.bisect_left(a, x)    # 第一个 >= x 的位置
i = bisect.bisect_right(a, x)   # 第一个 > x 的位置
bisect.insort(a, x)             # 插入并保持有序（查找 O(logn)，移动 O(n)）
```

场景：

- 300 最长递增子序列（耐心排序 + `bisect_left`）
- 二分答案、查找区间
- 「小于等于 x 的个数」= `bisect_right(a, x)`
- 「大于等于 x 的个数」= `len(a) - bisect_left(a, x)`

```python
# 300. 最长递增子序列 O(n log n)
tails = []
for x in nums:
    i = bisect.bisect_left(tails, x)
    if i == len(tails):
        tails.append(x)
    else:
        tails[i] = x
return len(tails)
```

---

## 九、functools

```python
from functools import lru_cache, cmp_to_key, reduce

@lru_cache(None)        # 或 py3.9+ 的 @cache
def dfs(i, j):
    ...
# 注意：参数必须可哈希（不能传 list，改传 tuple 或 str）
# 多组用例间记得 dfs.cache_clear()
```

| 工具 | 用途 | 场景 |
|---|---|---|
| `@lru_cache(None)` | 记忆化递归 | 509 斐波那契、70 爬楼梯、322 零钱兑换、矩阵路径 |
| `cmp_to_key` | 自定义比较器排序 | 179 最大数、自定义规则排序 |
| `reduce` | 累积归约 | 较少用，通常 `sum` / 循环更清晰 |

⚠️ 被 `@lru_cache` 装饰的函数若返回可变对象，调用方**不要修改返回值**，否则污染缓存。
需要可变返回时先拷贝。

---

## 十、itertools

```python
from itertools import accumulate, combinations, permutations, product, groupby

list(accumulate(nums))              # 前缀和 → 560 和为K的子数组
list(accumulate(nums, initial=0))   # 带前导 0，方便算区间和
combinations(nums, k)               # 组合（不考虑顺序、不重复）
permutations(nums, k)               # 排列（考虑顺序）
product([0, 1], repeat=n)           # 笛卡尔积 / 子集暴力
groupby(sorted_list, key=...)       # 分组，**必须先排序**
```

⚠️ 排列组合是**指数级复杂度**，只能用于 n ≤ 10 左右的小数据，大了必 TLE。

```python
# 560. 和为 K 的子数组
from collections import Counter
pre = Counter()
pre[0] = 1
s = ans = 0
for x in nums:
    s += x
    ans += pre[s - k]
    pre[s] += 1
```

---

## 十一、数学 / 位运算 / 边界值

```python
INF = float('inf')          # 正无穷，用于初始化「最小值距离 / 最大答案」
NEG = float('-inf')

import math
math.gcd(a, b)              # 最大公约数（3.9+ 支持 math.gcd(*list)）
math.lcm(a, b)              # 最小公倍数（3.9+）
math.isqrt(n)               # 整数平方根，向下取整（比 int(math.sqrt(n)) 精确，避免浮点误差）
math.sqrt(n) / math.log(x, 2) / math.factorial(n)

abs(x)
divmod(a, b)                # → (商, 余数)，一次拿到两个
pow(a, b, mod)              # 快速幂取模 O(log b)，远快于 a**b % mod
```

### 位运算

```python
x & (x - 1)                 # 消去最低位的 1 → 统计 1 的个数、判断 2 的幂
x & -x                      # 取出最低位的 1
(n >> i) & 1                # 取第 i 位
bin(x)                      # → '0b1010'
bin(x).count('1')           # 数 1 的个数（3.10+ 可用 x.bit_count()）
int('1010', 2)              # 二进制字符串 → 整数
x << 1 / x >> 1             # 乘 2 / 除 2
```

```python
# 191. 位 1 的个数
count = 0
while n:
    n &= n - 1
    count += 1

# 231. 2 的幂
return n > 0 and (n & (n - 1)) == 0
```

> ⚠️ `round(2.5)` = 2（银行家舍入，向偶数靠）。需要常规四舍五入用 `int(x + 0.5)` 或 `Decimal`。

---

## 十二、递归 / 输入板子

```python
import sys
sys.setrecursionlimit(10**6)    # 深递归（树的直径、DFS）必须加，否则爆栈

from typing import List, Dict, Set, Tuple, Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ...
```

`typing` 常用：`List[int]`、`Dict[str, int]`、`Set[int]`、`Tuple[int, int]`、`Optional[ListNode]`。

---

## 十三、高频一句话模板

```python
# 1) 二维网格四方向遍历（岛屿、迷宫）
for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    nx, ny = x + dx, y + dy
    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
        ...

# 2) 单调栈（496 下一个更大元素）
for x in nums:
    while stack and nums[stack[-1]] < x:
        ans[stack.pop()] = x
    stack.append(idx)

# 3) 回溯骨架（子集 / 组合 / 全排列）
def dfs(start, path):
    res.append(path[:])          # 注意要拷贝！
    for i in range(start, len(nums)):
        path.append(nums[i])
        dfs(i + 1, path)
        path.pop()

# 4) 并查集
parent = list(range(n))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])     # 路径压缩
    return parent[x]
def union(a, b):
    parent[find(a)] = find(b)

# 5) 双指针（有序数组两数之和）
l, r = 0, len(nums) - 1
while l < r:
    s = nums[l] + nums[r]
    if s == target: return [l, r]
    elif s < target: l += 1
    else: r -= 1

# 6) 滑动窗口
l = 0
for r, x in enumerate(s):
    window[x] += 1
    while 不满足条件:
        window[s[l]] -= 1
        l += 1
    ans = max(ans, r - l + 1)

# 7) 二分答案（左闭右开写法）
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid): hi = mid
    else: lo = mid + 1
return lo
```

---

## 十四、五个高频坑

| # | 坑 | 正确写法 |
|---|---|---|
| 1 | `[[0]*n]*m` 所有行共享引用，改一行全变 | `[[0]*n for _ in range(m)]` |
| 2 | `pop(0)` / `insert(0, x)` 是 O(n) | 换 `collections.deque` |
| 3 | 循环里字符串 `+=` 拼接是 O(n²) | 先 `append` 到 list，最后 `''.join(...)` |
| 4 | 递归深度 > 1000 直接 RE | 加 `sys.setrecursionlimit(10**6)` |
| 5 | 遍历 dict / list 时增删元素 | 先快照 `for k in list(d.keys())` |

补充：

- 判断空栈 / 空串一定要先判空：`while stack and stack[-1].isdigit():`
- `list.index(x)` 是 O(n)，别在循环里用
- `sorted` 每次都产生新列表，循环里反复排序会拖慢
- 用 `@lru_cache` 时参数不能有 list / dict（不可哈希）

---

## 附录：按题型反查工具

| 题型 | 优先想到的工具 |
|---|---|
| 括号匹配、表达式解析 | `list` 当栈、`isdigit()`、`ord/chr` |
| 下一个更大元素、柱状图最大矩形 | 单调栈 `while stack and ...` |
| 二叉树层序、BFS 最短路 | `deque` + `popleft` |
| 回溯、全排列、子集 | `path[:]` 拷贝、`itertools.permutations`（小数据） |
| 记忆化搜索、DP | `@lru_cache(None)` |
| TopK、第 K 大、合并 K 路 | `heapq`（大顶堆存负数） |
| 有序数组查找、LIS | `bisect_left / bisect_right` |
| 异位词、频次统计 | `Counter`、长度 26 的 `ord` 数组 |
| 前缀和、子数组和 | `itertools.accumulate` + `Counter` |
| 去重、查补数 | `set`，O(1) `in` |
| 图 / 并查集 | `defaultdict(list)` 邻接表、路径压缩 `find` |
| 位运算技巧题 | `x & (x-1)`、`x & -x`、`bin().count('1')` |
| 区间合并、扫描线 | `sorted(key=lambda x: x[0])` |
| 快速幂、取模 | `pow(a, b, mod)` |
| 最小值初始化 | `float('inf')` |

---

**参考示例**：`medium/leetcode-394.py` 里有 `isdigit()` + 栈的完整实战代码与逐行注释。
