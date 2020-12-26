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
- 堆化，正序构建大顶堆，逆序构建小顶堆
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

### 其他类似题目：
- [703. 数据流中的第 K 大元素](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/)
> 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
<details>
	<summary>解法</summary>
	
本题是流动的**数据流**，所以只能用**堆排算法**.
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # 加入-Inf, 防止初始时heappushpop([], -2)，此时nums=[], nums[0]报错
        self.nums = heapq.nlargest(k, nums + [float('-Inf')])
        heapq.heapify(self.nums)


    def add(self, val: int) -> int:
        heapq.heappushpop(self.nums, val)
        return self.nums[0]
```
</details>

- [295. 数据流的中位数](https://leetcode-cn.com/problems/find-median-from-data-stream/)
> 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，
```
[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
```
<details>
	<summary>解法</summary>
	
```python
# 方法一： 直接二分插入，维持原来的数组有序
# 复杂度为 O(nlogn)

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        

    def addNum(self, num: int) -> None:
        # 二分插入，使得原数组维持有序
        bisect.insort_left(self.arr, num)
        

    def findMedian(self) -> float:
        n = len(self.arr)
        # 无论原数组长度为奇或偶，求中位数都是这个表达式
        return (self.arr[n // 2] + self.arr[(n - 1) // 2]) / 2.0
        

# 方法二：原数组前半段用大顶堆来维护，后半段用小顶堆来维护
# 复杂度为 O(logn)
# 比如 [1, 2, 3][4, 8] 或者 [1, 2, 3][4, 8, 10] 前半段递增只关心最大的值3， 后半段只关心4
# 所以[1, 2, 3]用大顶堆来维护， [4, 8, 10]用小顶堆来维护


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num: int) -> None:
        self.size += 1
        # 因为 (前半段长度 >= 后半段长度)， 所以add的元素优先补冲到后半段
        # 新add的元素，从前半段“游走”一遍后加入后半段，维护了数组递增
        _, max_top = heapq.heappushpop(self.maxheap, (-num, num))
        heapq.heappush(self.minheap, max_top)
        # 再来看整体长度，如果是奇数长度，则上面的操作使得 (前半段长度 < 后半段长度)
        # 需要从后半段匀出来一个，放到前半段
        if self.size & 1 == 1:
            min_top = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, (-min_top, min_top))
        

    def findMedian(self) -> float:
        # 前半段大顶堆存的 tumple
        if self.size & 1 == 1:
            return self.maxheap[0][1]
        else:
            return (self.maxheap[0][1] + self.minheap[0]) / 2.0
```
</details>


# 归并排序

<details>
    <summary>迭代版本-Java</summary>
    
```java
import java.lang.Math;


public class MergeSort {
    public void sort(int[] arr) {

        if(arr == null) return;

        int[] temp = new int[arr.length];
        int left_min, left_max, right_min, right_max;

        //步长 
        for(int i = 1; i < arr.length; i = i * 2) {
            for(left_min = 0; left_min < arr.length - i; left_min = right_max) {

                left_max = right_min = left_min + i;
                right_max = Math.min(arr.length, right_min + i);

                int t = 0;
                while(left_min < left_max && right_min < right_max) {
                    temp[t++] = arr[left_min] < arr[right_min]? arr[left_min++]: arr[right_min++];
                }

                //如果Lmin 没有走到LMAX的位置 说明L还有元素 
                while(left_min < left_max) {
                    arr[--right_min] = arr[--left_max];
                }

                while(t > 0) {
                    //把整个数组还原到 刚刚剩下那个最大元素的后面 
                    arr[--right_min] = temp[--t];
                }
            }
        }
    }
}
```

</details>


<details>
    <summary>递归版本-python</summary>
    
```python
class Solution:

    def merge_sort(self, nums):
        if len(nums) <= 1: return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)
    

    def merge(self, left, right):
        i, j = 0, 0
        tmp = []
        while i < len(left) or j < len(right):
            if j == len(right) or i < len(left) and left[i] <= right[j]:
                tmp.append(left[i])
                i += 1
            else:
                tmp.append(right[j])
                j += 1
        return tmp
```
</details>

<details>
    <summary>递归版本-Java</summary>
    
```java
package sortdemo;

import java.util.Arrays;

/**
 * Created by chengxiao on 2016/12/8.
 */
public class MergeSort {
    public static void main(String []args){
        int []arr = {9,8,7,6,5,4,3,2,1};
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }
    public static void sort(int []arr){
        int []temp = new int[arr.length];//在排序前，先建好一个长度等于原数组长度的临时数组，避免递归中频繁开辟空间
        sort(arr,0,arr.length-1,temp);
    }
    private static void sort(int[] arr,int left,int right,int []temp){
        if(left<right){
            int mid = (left+right)/2;
            sort(arr,left,mid,temp);//左边归并排序，使得左子序列有序
            sort(arr,mid+1,right,temp);//右边归并排序，使得右子序列有序
            merge(arr,left,mid,right,temp);//将两个有序子数组合并操作
        }
    }
    private static void merge(int[] arr,int left,int mid,int right,int[] temp){
        int i = left;//左序列指针
        int j = mid+1;//右序列指针
        int t = 0;//临时数组指针
        while (i<=mid && j<=right){
            if(arr[i]<=arr[j]){
                temp[t++] = arr[i++];
            }else {
                temp[t++] = arr[j++];
            }
        }
        while(i<=mid){//将左边剩余元素填充进temp中
            temp[t++] = arr[i++];
        }
        while(j<=right){//将右序列剩余元素填充进temp中
            temp[t++] = arr[j++];
        }
        t = 0;
        //将temp中的元素全部拷贝到原数组中
        while(left <= right){
            arr[left++] = temp[t++];
        }
    }
}
```

</details>

### 相关题目:
- [327. 区间和的个数](https://leetcode-cn.com/problems/count-of-range-sum/)
- [315. 计算右侧小于当前元素的个数](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/)
- [剑指 Offer 51. 数组中的逆序对](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/)
- [148. 排序链表](https://leetcode-cn.com/problems/sort-list/)

### 参考：
- [排序——归并排序（递归实现+迭代实现 ）](https://www.cnblogs.com/xieyupeng/p/7045988.html)
- [图解排序算法(四)之归并排序](https://www.cnblogs.com/chengxiao/p/6194356.html)


# 自定义排序
- python3中的自定义排序方法
```python

import functools
 
strs=[3,4,1,2]
 
#自定义排序规则
def my_compare(x,y):
    if x>y:
        return 1
    elif x<y:
        return -1
    return 0
# 自定义排序结果
new_strs = sorted(strs,key=functools.cmp_to_key(my_compare))
```
- [179. 最大数](https://leetcode-cn.com/problems/largest-number/)
> 给定一组非负整数 `nums`，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。			
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。			

示例 1：
```
输入：nums = [10,2]
输出："210"
```
<details>
    <summary>解法</summary>
    
```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 自定义排序规则
        def my_comparison(x, y):
            x, y = str(x), str(y)
            if x + y > y + x:
                return 1
            else:
                return -1
        # 逆序排列
        nums.sort(key=functools.cmp_to_key(my_comparison), reverse=True)
        nums = [*map(str, nums)]
        return ''.join(nums) if nums[0] != '0' else '0'
```
</details>
