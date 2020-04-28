class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums = [[x, y] for x in nums1[:min(k, len(nums1))] for y in nums2[:min(k, len(nums2))]]
        return heapq.nsmallest(min(k, len(nums)), nums, key=sum)
