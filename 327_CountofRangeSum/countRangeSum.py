class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0] * (len(nums) + 1)
        for i in range(1, len(presum)):
            presum[i] = presum[i - 1] + nums[i - 1]
        
        def merget_sort(nums):
            if len(nums) < 2:
                return nums
            mid = len(nums) // 2
            left = merget_sort(nums[:mid])
            right = merget_sort(nums[mid:])
            return merge(left, right)
        
        self.cnt = 0

        def merge(left, right):
            i = 0
            jl, ju = 0, 0
            while i < len(left):
                while jl < len(right) and right[jl] - left[i] <= upper: jl += 1
                while ju < len(right) and right[ju] - left[i] < lower: ju += 1
                self.cnt += jl - ju
                i += 1
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

        merget_sort(presum)
        return self.cnt
