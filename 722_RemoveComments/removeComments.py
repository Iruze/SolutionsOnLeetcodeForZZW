class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # sign=1表示前面有了'/*'，sign=0则表示没有
        sign = 0
        ans = []
        for line in source:
            # 不是继续前面的'/*'，则是新的一行
            if sign == 0: 
                cur = ''
            i = 0
            while i < len(line):
                if sign == 0 and line[i:i+2] == '/*':
                    sign += 1
                    i += 1
                elif sign == 1 and line[i:i+2] == '*/':
                    sign -= 1
                    i += 1
                elif sign == 0 and line[i:i+2] == '//':
                    break
                elif sign == 0:
                    cur += line[i]
                i += 1
            # 若'/*' 和 '*/'完全闭合
            if cur and sign == 0:
                ans.append(cur[:])
        return ans
