# 时间复杂度为O(N3), 空间复杂度为O(N)
# i1, i2作为固定的两个索引, i3, i4作为双指针
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        # 这类x数相加，一般都是1.先排序, 2. 双指针
        nums.sort()
        # 当target大于nums的最大4数和, 或小于最小4数和
        if target < sum(nums[:4]) or sum(nums[-4:]) < target:
            return []
        res = []
        n = len(nums)
        for i1 in range(n - 3):
            # 当target小于i1时候的最小4数和
            if target < nums[i1] + nums[i1 + 1] + nums[i1 + 2] + nums[i1 + 3]:
                break
            # 当target大于i1时候的最大4数和
            if nums[i1] + sum(nums[-3:]) < target:
                continue
            # 避免i1重复
            if 0 <= i1 - 1 and nums[i1] == nums[i1 - 1]:
                continue
            for i2 in range(i1 + 1, n - 2):
                # 当target小于i2时候的最小4数和
                if target < nums[i1] + nums[i2] + nums[i2 + 1] + nums[i2 + 2]:
                    break
                # 当target大于i2时候的最大4数和
                if nums[i1] + nums[i2] + sum(nums[-2:]) < target:
                    continue
                # 避免i2重复
                if i1 < i2 - 1 and nums[i2] == nums[i2 - 1]:
                    continue
                i3, i4 = i2 + 1, n - 1
                while i3 < i4:
                    # 避免i3重复
                    if i2 < i3 - 1 and nums[i3] == nums[i3 - 1]:
                        i3 += 1
                        continue
                    # 避免i4重复
                    if i4 + 1 < n and nums[i4] == nums[i4 + 1]:
                        i4 -= 1
                        continue
                    total = nums[i1] + nums[i2] + nums[i3] + nums[i4]
                    # i3向右, i4向左
                    if total < target:
                        i3 += 1
                    elif total > target:
                        i4 -= 1
                    else:
                        res.append([nums[i1], nums[i2], nums[i3], nums[i4]])
                        i3, i4 = i3 + 1, i4 - 1
        return res
