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
        
