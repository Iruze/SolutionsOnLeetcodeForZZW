# 方法一：基于归并排序
# O(m + n)时间复杂度， O(1)空间复杂度
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i，j分别指向nums1, nums2的尾部，
        # t指向nums1的长度m+n处
        i, j, t = m - 1, n - 1, m + n - 1           
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[t] = nums2[j]
                j -= 1
            else:
                nums1[t] = nums1[i]
                i -= 1
            t -= 1
        while i >= 0:
            nums1[t] = nums1[i]
            t, i = t - 1, i - 1
        while j >= 0:
            nums1[t] = nums2[j]
            t, j = t - 1, j - 1
            
# 方法二：基于插入排序
# O(m * n)时间复杂度，O(1)空间复杂度
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            j = i 
            # 将nums2的当前第一个元素复制到nums1排序后下一个元素，这样方便在while循环中应用同一个j
            nums1[j] = nums2[i - m]
            while j > 0 and nums1[j] < nums1[j - 1]:
                nums1[j], nums1[j - 1] = nums1[j - 1], nums1[j]
                j -= 1
