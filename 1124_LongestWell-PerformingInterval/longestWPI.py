class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ans = 0
        cnt = 0
        # pos记录cnt首次出现的位置
        pos = dict()
        for i, h in enumerate(hours):
            # 有点像摩尔投票法（前面的题有用到）
            if h > 8:
                cnt += 1
            else:
                cnt -= 1
            if cnt > 0:
                ans = i + 1
            else:
                # 贪心：当前的cnt值首次出现，记录其位置，即记录cnt索引的最小值
                if cnt not in pos: pos[cnt] = i
                # 贪心思想：如果cnt - 1在pos中存在且索引为j(j必然小于i)，
                # 则[j+1, i]区间有： cnt = 1 > 0
                if cnt - 1 in pos: ans = max(ans, i - pos[cnt - 1])
        return ans
        
