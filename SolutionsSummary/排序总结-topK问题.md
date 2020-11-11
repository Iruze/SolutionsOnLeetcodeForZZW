# 堆排序

## 二叉堆的**上浮**和**下沉**

1). 在讲**堆排序**之前，先来复习一下另外两种排序，**冒泡排序**和**插入排序**。

<details>
    <summary>冒泡排序</summary>
    
```python
def bubbleSort(nums):
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
```
</details>
 
2). **插入排序**的写法跟如上的**冒泡排序**类似，但是思想却完全不同.

<details>
    <summary>直接插入排序</summary>
    
参考： [白话经典算法系列之二 直接插入排序的三种实现](https://blog.csdn.net/MoreWindows/article/details/6665714#commentBox)    
```python
 def insertSort(nums):
    for i in range(1, len(nums)):
        for j in range(i - 1, -1, -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            else:
                break
```
</details>

3). 再来看**堆排序**里面的**上浮**和**下沉**
    
堆排序-上浮    
```python
# 大顶堆， logn次比较, logn次交换
def swim(nums, k):
	while k > 0 and nums[k] > nums[(k - 1) // 2]:
		nums[k], nums[(k - 1) // 2] = nums[(k - 1) // 2], nums[k]
		k = (k - 1) // 2     
```

堆排序-下沉
    
```python
# 大顶堆， 2logn次比较, logn次交换
def sink(nums, k):
	while 2 * k + 1 < len(nums):
		j = 2 * k + 1
		if j + 1 < len(nums) and nums[j] < nums[j + 1]:
			j += 1
		if nums[j] < nums[k]:
			break
		nums[j], nums[k] = nums[k], nums[j]
		k = j     
```

## 堆排序

**步骤：**
- 堆化，正序构建小顶堆，逆序构建大顶堆
- 堆顶节点和尾节点互换，从堆顶节点开始`sink`下沉
- 重复上一个步骤

**ps:**
- 如果堆数组是            
基`0`：          
父节点：`(i-1)//2`， 子节点：`2*i+1`, `2*i+2`                    
基`1`:           
父节点：`i//2`, 子节点：`2*i`, `2*i+1`        

<details>
    <summary>code</summary>
    
```python
class Solution:
    	
    def __init__(self):
        pass

    # 正序排序
    def sort(self, nums):
        n = len(nums)
        # a)堆化, 从 n/2 -1 处开始, 一共有 O(2n)次比较, O(n)次交换
        # 大顶堆， 每个节点最多被比较2次（自己-子节点， 自己-父节点），最多交换1次
        for i in range(n // 2 - 1, -1, -1):
            self._sink(nums, i, n)
        
        # b)首尾交换,而后从 0 处开始下沉, 一共 O(2nlogn) 次比较, O(nlogn)次交换
        for j in range(n - 1, 0, -1):
            nums[0], nums[j] = nums[j], nums[0]
            self._sink(nums, 0, j)

    # 构建大顶堆，单次下沉- O(2logn) 次比较, O(logn) 次交换
    def _sink(self, nums, i, n):
        while 2 * i + 1 < n:
	    j = 2 * i + 1
            if j + 1 < n and nums[j] < nums[j + 1]:
                j += 1
            if nums[i] > nums[j]:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i = j    
```

</details>


综合如上分析，堆排序的时间复杂度为 `O(2n + 2nlogn)` 次比较, 一半的次数交换, 即 `O(nlong)` 的复杂度



- 参考

    <details>
        <summary>展开</summary>

    1) 红宝书-算法(第四版)

    2) [图解排序算法(三)之堆排序](https://www.cnblogs.com/chengxiao/p/6129630.html)

    3) [白话经典算法系列之七 堆与堆排序](https://blog.csdn.net/MoreWindows/article/details/6709644)

    </details>

# 快排
## partition模块
**partition**的时间复杂度为`O(n)`， 即调用一次**partition**遍历`end-start`长的`nums`.
```python
def partition(nums, start, end):
    # 在[start, end]区间内找到随机的起始下标
    idx = random.randint(start, end)
    # 基准值置换放到最后
    nums[idx], nums[end] = nums[end], nums[end]
    small = start - 1
    for i in range(start, end):
        if nums[i] < nums[end]:
            small += 1
            if small != i:
                nums[small], nums[i] = nums[i], nums[small]
    small += 1
    # 恢复基准值的位置
    nums[small], nums[end] = nums[end], nums[small]
    return small
```

## 快排
快排基于上面的`partition`模块        
- `partition`找到基准分界的下标`idx`
- **分治思想**： 将`nums`分为`idx`左右两部分，分别再次调用`partition`
<details>
    <summary>展开</summary>
    
```python
def quickSort(self, nums, start, end):
    if start == end:
        return
    idx = self._partition(nums, start, end)
    if idx > start:
        self._partition(nums, start, idx - 1)
    if idx < end:
        self._partition(nums, idx + 1, end)
```
</details>

时间复杂度
> 最好时间复杂度： `O(nlogn)`, 平均时间复杂度: `O(nlogn)`
>
> 最坏时间复杂度： `O(n*n)`, 退化成**冒泡排序**，发生条件： 
>1. 已排序； 
>2. 所有元素相等；
>3. `idx=random.randint(start, end)`，每次`idx=end`，使得另一边的部分始终为空`[]`.


# topK问题
|       解法          |      平均时间复杂度      |                缺点                  |    
|       :----        |        :----          |                  :----               |
|       partition算法 |         `O(n)`        |       改变元素顺序，海量数据时占用内存     |
|       堆排          |      `O(nlogk)`           |       不改变元素顺序，适合处理海量数据     |



- [面试题 17.14. 最小K个数](https://leetcode-cn.com/problems/smallest-k-lcci/)
> 设计一个算法，找出数组中最小的`k`个数。以任意顺序返回这`k`个数均可。

示例：
```shell
输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
```
### I. partitiona解法
<details>
	<summary>code</summary>
	
```python
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        def partition(arr, start, end):
            idx = random.randint(start, end)
            arr[idx], arr[end] = arr[end], arr[idx]
            small = start - 1
            for i in range(start, end):
                if arr[i] < arr[end]:
                    small += 1
                    if small != i:
                        arr[small], arr[i] = arr[i], arr[small]
            small += 1
            arr[small], arr[end] = arr[end], arr[small]
            return small
        if not arr or k < 1: return []
        start, end = 0, len(arr) - 1
        idx = partition(arr, start, end)
        while idx != k - 1:
            if idx < k - 1:
	    	# 错误写法: idx = partition(arr, idx + 1, end)
		# start, end在每一次的搜索中都在缩写范围，故这两个边界应该是实际赋值
                start = idx + 1
                idx = partition(arr, start, end)
            else:
                end = idx - 1
                idx = partition(arr, start, end)
        return arr[:k]
```
</details>

> 时间复杂度分析:	
>
>
> `partition`单次调用的时间复杂度为`O(n)`，当`idx`多次随机调用时候，可认为将长度为`n`的数组每次折半搜索`k`，即:	
>
> `1 + 1/2 + 1/4 + 1/8 + ... = 2 - 1/2^n < 2`，即时间不超过`O(2n)`，故**总的随机调用**时间复杂度为`O(n)`.

### II. 堆排解法

<details>
	<summary>code</summary>
	
```python
def smallestK(self, arr: List[int], k: int) -> List[int]:
        ans = []
        for a in arr:
            if len(ans) < k:
	    	# python只有最小堆，故元素取反，等效于建立a实际值的最大堆
                heapq.heappush(ans, -a)
            else:
                heapq.heappushpop(ans, -a)
        return [-x for x in ans]
```

</details>

> 时间复杂度分析:
>
>
> 先建堆，长度为`k`的堆，`O(k)`，后面的数字进入堆，每次堆调整为`O(logk)`，
>所以总的时间复杂度为: `O(k) + O(n*logk)`
