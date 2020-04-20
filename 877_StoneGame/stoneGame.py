class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 石子按下标分为奇偶堆，这两堆必然有一堆总数大于另一堆
        # 先瞄好是奇数堆多，还是偶数堆多
        # 先手能够决定拿奇偶数堆，所以先手必胜
        return True
