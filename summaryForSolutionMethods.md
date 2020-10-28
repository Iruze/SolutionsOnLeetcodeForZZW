### 求两个数的最大公约数
- 欧几里得辗转相除法（递归实现）
```python
def gcd(p, q):
    if q == 0: 
        return p
    return gcd(q, p % q)
```
例：[365. 水壶问题](https://leetcode-cn.com/problems/water-and-jug-problem/)
> 有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
你允许：    
装满任意一个水壶        
清空任意一个水壶   

>从一个水壶向另外一个水壶倒水，直到装满或者倒空         
示例 1: (From the famous "Die Hard" example)          
输入: x = 3, y = 5, z = 4         
输出: True   

> 示例 2:                   
输入: x = 2, y = 6, z = 5         
输出: False           
解法：
```sql
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return z == 0 or x + y >= z and z % math.gcd(x, y) == 0
```

### 堆排序代码
- 参考《算法》， 构建**最大堆**，对数组`nums`进行**升序**排列
```python
# 上浮
def swim(nums, k, N):
	while k > 1 and less(k // 2, k):
		exch(k // 2, k)
		k //= 2


# 下沉
def sink(nums, k, N):
	while 2 * k <= N:
		j = 2 * k
		if j < N and less(j, j + 1): j += 1
		if less(j, k): break
		exch(k, j)
		k = j


# 堆排序
def heapSort(nums):
	N = len(nums)
	# 构建堆
	for k in range(k // 2, 0, -1):
		sink(nums, k, N)
	# 堆排序
	while N > 1:
		exch(1, N)
		N -= 1
		sink(nums, 1, N)
```
