# 参考解法：
# https://leetcode-cn.com/problems/minimum-swaps-to-make-strings-equal/solution/java-tan-xin-suan-fa-xiang-jie-zhi-xing-yong-shi-n/
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        # 统计xy和yx的对数，最终的交换次数为：(xy + 1) // 2 + (yx + 1) // 2
        for i, v in enumerate(s1):
            # 贪心思想：相等是无需交换
            if s1[i] == s2[i]:
                continue
            elif s1[i] == 'x':
                xy += 1
            else:
                yx += 1
        # xy和yx的和必须是偶数
        return (xy + 1) // 2 + (yx + 1) // 2 if (xy + yx) & 1 == 0 else -1
