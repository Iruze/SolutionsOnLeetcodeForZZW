"""
1. 先排序，对words的每一个字符串w按照从大到小排列
2. 如果words中的某个字符w，使得w+'#'不在S中，则S中需要加入w+'#'；否则跳过
"""
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        S = ''
        # 从大到小排序
        words.sort(key=lambda x:len(x), reverse=True)
        for w in words:
            # 必须是 w+'#'，不能是仅是w
            if w + '#' not in S:
                S += w + '#'
        return len(S)
