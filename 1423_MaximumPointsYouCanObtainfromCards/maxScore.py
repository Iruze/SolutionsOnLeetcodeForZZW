class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        start, end = 0, sum(cardPoints[-k:])
        ans = start + end
        # 滑动窗口，维护数组两端长度为k
        for i in range(k):
            start += cardPoints[i]
            end -= cardPoints[-(k - i)]
            ans = max(ans, start + end)
        return ans
