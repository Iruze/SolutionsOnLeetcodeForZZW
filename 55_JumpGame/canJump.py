class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # 自顶向下
        # end = 0
        # for idx in range(len(nums)):
        #     if end < idx:
        #         return False
        #     end = max(end, idx + nums[idx])
        #     if end >= len(nums) - 1:
        #         return True
        # return False

        # 自底向上
        start, end = len(nums) - 2, len(nums) - 1
        while start >= 0:
            if start + nums[start] >= end:
                end = start
            start -= 1
        return end <= 0
