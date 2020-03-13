# 摩尔投票法变题
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = 0, 0
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num != num2 and (cnt1 == 0 or num == num1):
                num1 = num
                cnt1 += 1
                continue
            if num == num2 or cnt2 == 0:
                num2 = num
                cnt2 += 1
                continue
            cnt1, cnt2 = cnt1 - 1, cnt2 - 1
        # 计算num1, num2的个数
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == num1: cnt1 += 1
            elif num == num2: cnt2 += 1
        ans = []
        # 判断是否是大于 1/3
        if cnt1 > len(nums) // 3: ans.append(num1)
        if cnt2 > len(nums) // 3: ans.append(num2)
        return ans
