"""
1. 以words中的每个子串为开头子串，在s中寻找开头子串的位置；
2. 哈希表记录了words中每个子串的个数，从开头子串开始，往后以单个子串长度为步进，滑动搜索s中的子串和哈希表中的子串匹配；
3. 如果哈希表中的子串全部被消耗完，证明这个开头子串是符合要求的结果
"""

class Solution:
    def findSubstring(self, s, words):
        ls, lw = len(s), sum(map(len, words))
        if ls == 0 or lw == 0 or lw > ls:
            return []
        lw_one, n = len(words[0]), len(words)
        words_dict = Counter(words)
        words_set = set(words_dict.keys())
        ans = []
        # words中每个字符为开头的子串，对这些开头挨个扫描
        for w in words_set:
            base = 0
            # 开头子串存在与否？
            while w in s[base:]:
                # 定位开头子串的位置
                idx = base + s[base:].index(w)
                # 总的串联子串的长度超过s的长度，不符合要求
                if idx + lw > ls:
                    break
                # s上对应于words中的单个子串为s[lo:hi+1]
                lo, hi = idx, idx + lw_one
                tmp_dict = words_dict.copy()
                while hi <= ls and s[lo:hi] in tmp_dict and tmp_dict[s[lo:hi]] > 0:
                    tmp_dict[s[lo:hi]] -= 1
                    lo += lw_one
                    hi += lw_one
                # s上以单个子串lw_one为步进扫描完后，也全部消耗完了tmp_dict中的子串，则判定为符合的串联子串
                if not any(tmp_dict.values()):
                    ans.append(idx)
                # s中以w开头的开头子串的位置可能不止一处，继续从idx + 1开始的索引之后寻找
                base = idx + 1
        return ans
