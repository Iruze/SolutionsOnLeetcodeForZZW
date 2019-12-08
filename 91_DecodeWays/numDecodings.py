class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':                                   # 01xxx 无效
            return 0
        f1, f2, f, n = 1, 1, 1, len(s)
        for i in range(1, n):                                      # 从1开始，len(s)<2，直接返回 f=1
            if s[i] == '0':                                        # 当前位是否为‘0’分类讨论
                if s[i - 1] == '1' or s[i - 1] == '2':             # 110x, 120x 时：f = f1
                    f = f1
                else:                                              # 100x, 130x 无效
                    return 0
            elif s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6':
                    f = f1 + f2                                    # 非边界，如：1212，1122
            f1, f2 = f2, f                                         # 下一次迭代设置
        return f
