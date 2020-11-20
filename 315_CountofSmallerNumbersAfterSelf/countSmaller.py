class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = []
        ans = [0] * len(nums)
        for idx, num in enumerate(nums):
            arr.append((idx, num))
        def merge_sort(arr):
            if len(arr) <= 1: return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        def merge(left, right):
            i, j = 0, 0
            tmp = []
            while i < len(left) or j < len(right):
                if j == len(right) or i < len(left) and left[i][1] <= right[j][1]:
                    tmp.append(left[i])
                    # 说明left[i][1] 大于 所有right[:j][1]
                    ans[left[i][0]] += j
                    i += 1
                else:
                    tmp.append(right[j])
                    j += 1
            return tmp
        merge_sort(arr)
        return ans
