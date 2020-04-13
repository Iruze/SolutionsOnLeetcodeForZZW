class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if nums[mid] == nums[mid - 1]:
                if (mid - lo + 1) & 1:
                    hi = mid - 2
                else:
                    lo = mid + 1
            elif nums[mid] == nums[mid + 1]:
                if (hi - mid + 1) & 1:
                    lo = mid + 2
                else:
                    hi = mid - 1
            else:
                return nums[mid]
        return nums[lo]
