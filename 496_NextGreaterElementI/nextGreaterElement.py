# 解法一：先reg，后从reg中检索nums1中的元素
# 时间复杂度： O(M + N), 空间负责度：O(N)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        reg = {}
        # reg记录nums2中每个数下一个更大元素
        # stack维护一个单调递减序列
        for i, v in enumerate(nums2):
            while stack and nums2[stack[-1]] < v:
                reg[nums2[stack.pop()]] = v
            stack.append(i)
        # 从reg中检索nums1中的每个元素
        res = []
        for num in nums1:
            if num in reg:
                res.append(reg[num])
            else:
                res.append(-1)
        return res
        


# 解法二： 直接在while，弹出栈的过程中判断 if num in nums1：
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        pos = dict()
        for i, num in enumerate(nums2):
            # 维护单调递减栈， num大于stack中的最后一个元素e
            # ， 则最后一个元素的目标元素是num，即 pos{e: num}
            while stack and num > nums2[stack[-1]]:
                pos[nums2[stack.pop()]] = num
            stack.append(i)
        # num在pos中找不到目标元素，则输出-1
        return [pos.get(num, -1) for num in nums1]
