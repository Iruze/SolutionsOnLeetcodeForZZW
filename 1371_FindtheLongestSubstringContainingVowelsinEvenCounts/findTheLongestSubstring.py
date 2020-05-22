class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # a, e, i, o, u 奇偶排列的一共32中状态，5个字符均为偶数定义为状态0
        # pre:{状态： 位置}
        pre = {0: -1}

        # 一个字符也没有，即aeiou个数均为0， 视为状态0
        state = 0
        ans = 0
        # 异或^是没有进位的加法， 当出现元音时，对应位的状态+1
        for i, c in enumerate(s):
            if c == 'a': state ^= 1
            elif c == 'e': state ^= 2
            elif c == 'i': state ^= 4
            elif c == 'o': state ^= 8
            elif c == 'u': state ^= 16

            # 如果[0, i]和[0, j]状态相同，则[i+1, j]一定是状态0
            if state in pre:
                ans = max(ans, i - pre[state])
            # 说明当前状态首次出现，记录其位置i
            else:
                pre[state] = i
        
        return ans
