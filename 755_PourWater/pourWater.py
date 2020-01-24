class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        for v in range(V):
            p, i = K, K
            # 向左边搜索，记下水滴能够停留的地方p
            while i > 0 and heights[i] >= heights[i - 1]:
                if heights[i] != heights[i - 1]:
                    p = i - 1
                i -= 1
            # 如果左边能够停留水滴，heights[i]加1
            if p != K:
                heights[p] += 1
                continue
            # 向右边搜索
            while i < len(heights) - 1 and heights[i] >= heights[i + 1]:
                if heights[i] != heights[i + 1]:
                    p = i + 1
                i += 1
            # 记下右边水滴停留的地方
            if p != K:
                heights[p] += 1
                continue
            # 如果左右边都没有，则原地自增
            heights[p] += 1
        return heights
