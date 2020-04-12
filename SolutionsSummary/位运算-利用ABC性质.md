**位运算ABC性质：**

```shell
若 A ^ B = C, 则：   
A ^ C = B
C ^ A = B
```

- [421. 数组中两个数的最大异或值](https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/)

```shell
给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 231 。

找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i,  j < n 。

你能在O(n)的时间解决这个问题吗？
```
示例:
```
输入: [3, 10, 5, 25, 2, 8]

输出: 28

解释: 最大的结果是 5 ^ 25 = 28.
```

```python3
"""
我们不关心是哪两个数的XOR得到的最大值，只是从第31位到0位，逐位假设当前位是1；
利用 <若 A^B=C， 则 C^A=B> 性质，如果不能得到C^A=B，者证明当前位是0
"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = 0
        ans = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            s = set()                   # s用来存储各个数(32位表示)的前i个前缀
            for num in nums:
                s.add(mask & num)
            temp = ans | (1 << i)       # 假设ans此时i位上是1
            for prefix in s:
                if temp ^ prefix in s:
                    ans = temp
        return ans
```
