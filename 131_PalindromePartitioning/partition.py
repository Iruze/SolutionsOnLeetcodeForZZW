class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def helper(s, tmp):
            if not s:
                ans.append(tmp)
            # 分割出来的第一个回文串的长度，最长为len(s)
            # 这样递归的时候s中剩下的就为空，触发base case
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])
        
        helper(s, [])
        return ans
