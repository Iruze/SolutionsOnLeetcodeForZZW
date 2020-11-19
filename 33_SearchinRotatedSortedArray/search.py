"""
python3，二分搜索
1. 利用[153. 寻找旋转排序数组中的最小值]找到最小值的索引p，将原数组划分为两个有序数组；
2. 在[0, p]二分搜索；
3. 在[p+1, len(nums) - 1]二分搜索
"""
```python3
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        lo, hi = 0, len(nums) - 1
        # 1. find the index of the smallest val
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        # 2. search in the [0, lo]
        idx = bisect.bisect_left(nums, target, 0, lo)
        if 0 <= idx <= lo and nums[idx] == target:
            return idx
        # 3. search in the [lo+1:len(nums)-1]
        idx = bisect.bisect_left(nums, target, lo, len(nums))
        if lo <= idx < len(nums) and nums[idx] == target:
            return idx
        return -1
```


# 解法二：
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
```
