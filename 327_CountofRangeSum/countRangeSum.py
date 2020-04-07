class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0
        # 前缀和第一个元素为0， 方便统计最终结果
        presum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            presum[i + 1] += presum[i] + nums[i]
        tmp = [0 for _ in range(len(presum) + 1)]
        return self.mergeSort(presum, 0, len(presum) - 1, lower, upper, tmp)
    
    def mergeSort(self, presum, start, end, lower, upper, tmp):
        if start < end:
            mid = start + ((end - start) >> 1)
            left = self.mergeSort(presum, start, mid, lower, upper, tmp)
            right = self.mergeSort(presum, mid + 1, end, lower, upper, tmp)
            cur = self.merge(presum, start, mid, end, lower, upper, tmp)
            return left + right + cur
        return 0
    
    def merge(self, presum, start, mid, end, lower, upper, tmp):
        # 第一阶段：统计cnt，一次遍历
        lo = start
        lw, up = mid + 1, mid + 1
        cnt = 0
        while lo <= mid:
            while up <= end and presum[up] - presum[lo] <= upper: up += 1
            while lw <= end and presum[lw] - presum[lo] < lower: lw += 1
            cnt += up - lw
            lo += 1
        # 第二阶段： 正式归并排序， 二次遍历
        i, j, t = start, mid + 1, 0
        while i <= mid and j <= end:
            if presum[i] < presum[j]:
                tmp[t] = presum[i]
                t, i = t + 1, i + 1
            else:
                tmp[t] = presum[j]
                t, j = t + 1, j + 1
        while i <= mid:
            tmp[t] = presum[i]
            t, i = t + 1, i + 1
        while j <= end:
            tmp[t] = presum[j]
            t, j = t + 1, j + 1
        t = 0
        while start <= end:
            presum[start] = tmp[t]
            t, start = t + 1, start + 1
        return cnt
