class Solution:
    def isNumber(self, s: str) -> bool:
        if not s: return False
        
        sl = re.split(r'[eE]', s.strip())
        # e前后不包含数字、s中含有多个e或E
        if '' in sl or len(sl) > 2:
            return False
        # e之后有空格
        if sl[0][-1] == ' ':
            return False
        try:
            float(sl[0])
        except:
            return False
        # 当s为正负inf的时候
        if abs(float(sl[0])) == float('inf'):
            return False
        if len(sl) == 2:
            # e之前有空格
            if sl[1][0] == ' ':
                return False
            try:
                int(sl[1])
            except:
                return False
        return True
