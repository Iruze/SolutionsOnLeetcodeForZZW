class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pre = -1
        for i in range(len(nums)):
            if nums[i] == val and pre < 0:
                pre = i
            if nums[i] != val and pre >= 0:
                nums[i], nums[pre] = nums[pre], nums[i]
                pre = pre + 1
        return len(nums) if pre < 0 else pre
