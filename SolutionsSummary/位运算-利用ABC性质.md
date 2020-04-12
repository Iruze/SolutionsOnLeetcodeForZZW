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
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = 0
        ans = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            s = set()
            for num in nums:
                s.add(mask & num)
            temp = ans | (1 << i)
            for prefix in s:
                if temp ^ prefix in s:
                    ans = temp
        return ans
```
