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
# 小顶堆， logn次比较, logn次交换
def swim(nums, i):
    j = (i - 1) // 2
    while j >= 0 and nums[i] < nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
        i = j
        j = (i - 1) // 2      
```

堆排序-下沉
    
```python
# 小顶堆， 2logn次比较, logn次交换
def sink(nums, i, n)
    tmp = nums[i]
    j = 2 * i + 1
    while j < n:
        if j + 1 < n and nums[j + 1] > nums[j]:
            j += 1
        if nums[i] < nums[j]:
            break
        nums[i] = nums[j]
        i = j
        j = 2 * i + 1
    nums[i] = tmp        
```

## 堆排序

**步骤：**
- 堆化，正序构建小顶堆，逆序构建大顶堆
- 堆顶节点和尾节点互换，从堆顶节点开始`sink`下沉
- 重复上一个步骤

**ps:**
- 如果堆数组是            
基`0`：          
父节点：`(i - 1) // 2`， 子节点：`2 * i`, `2 * i + 1`                    
基`1`: 父节点：`i // 2`, 子节点：`2 * i`, `2 * i + 1`        

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
        j = 2 * i + 1
        tmp = nums[i]
        while j < n:
            if j + 1 < n and nums[j] < nums[j + 1]:
                j += 1
            if nums[i] > nums[j]:
                break
            nums[i] = nums[j]
            i = j
            j = 2 * i + 1
        nums[i] = tmp      
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
