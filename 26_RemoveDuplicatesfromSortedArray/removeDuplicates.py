class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快慢指针解法，pre指向当前不重复元素
        pre = 0
        for idx, num in enumerate(nums):
            if idx > pre and nums[idx] != nums[pre]:
                pre += 1
                nums[pre] = nums[idx]
        return pre + 1
