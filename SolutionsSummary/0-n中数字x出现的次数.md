# 题目：求 `0~n` 的所有自然序列中，数字 `x` 出现的次数

- [面试题43. 1～n整数中1出现的次数](https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/)
- [面试题 17.06. 2出现的次数](https://leetcode-cn.com/problems/number-of-2s-in-range-lcci/)

# 万能公式：
```python3
while i <= n:
  a, b = n // i, n % i
  ans += (a + m) // 10 * i + (b + 1 if a % 10 == x else 0)
  i *= 10
```
其中，`m = 9 - x`.

# 具体来讨论
以 [面试题 17.06. 2出现的次数](https://leetcode-cn.com/problems/number-of-2s-in-range-lcci/)为例：

> 编写一个方法，计算从 `0` 到 `n` (含 `n`) 中数字 `2` 出现的次数。

示例:
```
输入: 25
输出: 9
解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)
```

**解析：** (参考: [C++解法，代码很简单，思路好理解](https://leetcode-cn.com/problems/number-of-2s-in-range-lcci/solution/cjie-fa-dai-ma-hen-jian-dan-si-lu-hao-li-jie-by-we/))
```shell
- i     a      b      res
- 1     324    0      (324+7)/10*1 + 0 = 33
- 10    32     4      (32+7)/10*10 + 5 = 35
- 100   3      24     (3+7)/10*100 = 100
```

`res`和为`168`即为所求

个位为`4`，`5>2`，故个位为`2`时，个位之前的取值有`0~32`共`33`种情况

十位为`2`，`2`为统计的数字，`2`为固定，百位取到`0~2`时各位才能取到`0~9`共`310`种情况，

而百位取`3`时，个位仅能取到`0~4`共五种情况，故为`30+5 = 35`种情况

百位为`3`，当百位取`2`时，后两位的取值有`0~99`共`100`种情况，故为`100`

同理，更大的数也是同理，`+7`是为特殊情况设计，当取值为`0`，`1`，`2`时不会产生进位，大于`2`时允许产生进位

