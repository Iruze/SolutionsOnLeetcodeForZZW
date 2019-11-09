class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pre = 0
        for i in range(len(nums)):
            if i - pre == 1:
                if nums[i] != nums[pre]:
                    pre = i
                continue
            elif i - pre > 1:
                if nums[i] == nums[pre]:
                    continue
                else:
                    pre += 1
                    nums[pre] = nums[i]
        return pre + 1 if nums else 0
