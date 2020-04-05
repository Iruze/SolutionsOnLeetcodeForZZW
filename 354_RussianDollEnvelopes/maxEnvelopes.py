# 二分法确定堆数

import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0
        # 对于宽度 w 相同的数对，要对其高度 h 进行降序排序
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [env[1] for env in envelopes]
        n = len(heights)
        # 初始化纸牌堆
        top = [0 for _ in range(n)]
        piles = 0
        for h in heights:
            # 找到应当插入的堆的索引
            idx = bisect.bisect_left(top, h, 0, piles)
            # 无论是新建堆，还是续接在已有的堆，都是更新堆顶的牌
            top[idx] = h
            # 最后一个索引，说明需要新建堆
            if idx == piles:
                piles += 1
        return piles
