class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        mid = bisect.bisect(arr, x)
        # mid = self._bisect(arr, x)
        lo, hi = mid - 1, mid
        # 以mid为原点，左右开始收入ans，借助了归并排序的思想
        while 0 <= lo and hi < len(arr) and k > 0:
            if x - arr[lo] <= arr[hi] - x:
                ans.insert(0, arr[lo])
                lo -= 1
            else:
                ans.append(arr[hi])
                hi += 1
            k -= 1
        # 当左边有剩余时
        while 0 <= lo and k > 0:
            ans.insert(0, arr[lo])
            lo -= 1
            k -= 1
        # 当右边有剩余时
        while hi < len(arr) and k > 0:
            ans.append(arr[hi])
            hi += 1
            k -= 1
        return ans

    # 自己实现 bisect()函数
    def _bisect(self, arr, x):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
