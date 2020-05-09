class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        d = dict()

        def backtrack(pattern, string):
            if not pattern: return not string
            p = pattern[0]
            for i in range(1, len(string) - len(pattern) + 2):
                substr, mapstr = string[:i], d.get(p)
                # 要么有d[p]且能匹配上，要么没有d[p]
                if substr == mapstr or not mapstr and substr not in d.values():
                    # 不管有没有，重新插入d[p]不影响d原来的状态
                    d[p] = substr
                    if backtrack(pattern[1:], string[i:]): return True
                    # 如果d中原来没有d[p]， 且pattern[1:]的路不通
                    # ，则证明插入d[p]这条路一开始就不通，撤销 d[p]
                    elif not mapstr: del d[p]
            return False
        
        return backtrack(pattern, str)
