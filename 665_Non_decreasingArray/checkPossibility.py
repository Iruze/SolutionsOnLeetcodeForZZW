class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        t1, t2 = nums[0], nums[1]
        once_changed = False
        if t1 > t2:
            t1 = t2 - 1
            once_changed = True
        for num in nums[2:]:
            if t2 <= num:
                t1, t2 = t2, num
            elif once_changed:
                return False
            else:
                once_changed = True
                if t1 <= num:
                    t2 = num
        return True
