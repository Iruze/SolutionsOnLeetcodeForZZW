class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return -float('Inf')
        lft, rht = 0, len(nums) - 1
        while lft < rht:
            mid = lft + ((rht - lft) >> 1)
            if nums[mid] > nums[rht]:
                lft = mid + 1
            elif nums[mid] < nums[rht]:
                rht = mid
            else:
                rht -= 1
        return nums[lft]
