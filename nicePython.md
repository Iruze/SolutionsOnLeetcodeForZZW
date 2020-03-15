### filter函数

> 验证 "A man, a plan, a canal: Panama" 是否为回文串，仅考虑字母&数字，不考虑大小写

```python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [*filter(str.isalnum, s.lower())]
        return s == s[::-1]
```

filter的用法：
> `filter()`也接收一个函数和一个序列。`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。

* `s.lower()`可作用于字符串s中的每一个字符
* `str.isalnum()` 判断字符是字母或者数字字符
* `*`用来解包，表示**取出每一个**，结合[]使用这里作用跟`list()`一样

```python3
>>> s
'A man, a plan, a canal: Panama'
>>> s.lower()
'a man, a plan, a canal: panama'
>>> str.isalnum('a')
True
>>> t = map(int, ['2', '3', '4'])
>>> t
<map object at 0x106fa98e0>
>>> [*t]
[2, 3, 4]
```

### zip函数，用于转置矩阵

- [5356. 矩阵中的幸运数](https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix/)

> 给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。             
幸运数是指矩阵中满足同时下列两个条件的元素：          
在同一行的所有元素中最小            
在同一列的所有元素中最大


示例 1：

```
输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
```

code:
```python3
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # 每一行的最小值集合
        mins = {min(rows) for rows in matrix}
        # 每一列的最大值集合
        maxes = {max(cols) for cols in zip(*matrix)}
        # 因为没有重复的数，取交集
        return list(mins & maxes)
```

zip函数：

```python3
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
u = zip(*xyz)
```

```shell
一般认为这是一个unzip的过程，它的运行机制是这样的：

在运行zip(*xyz)之前，xyz的值是：[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

那么，zip(*xyz) 等价于 zip((1, 4, 7), (2, 5, 8), (3, 6, 9))

所以，运行结果是：[(1, 2, 3), (4, 5, 6), (7, 8, 9)]

注：在函数调用中使用*list/tuple的方式表示将list/tuple分开，作为位置参数传递给对应函数（前提是对应函数支持不定个数的位置参数).
```
