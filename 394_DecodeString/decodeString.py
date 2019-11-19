class Solution:
    def decodeString(self, s: str) -> str:
        stack = ['']
        for me in s:
            if '0' <= me and me <= '9':
                if stack and type(stack[-1]) == int:
                    stack[-1] = int(str(stack[-1]) + me)
                else:
                    stack.append(int(me))
            elif me == '[':
                stack.append('')
            elif 'a' <= me and me <= 'z' or 'A' <= me and me <= 'Z':
                stack[-1] += me
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                stack[-1] += top1 * top2
        return stack[0]
        
''' ‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’
# 输入样例
2[abc]3[cd]ef:

[‘’]
[‘’, 2]
[‘’, 2, ‘’]
[‘’, 2, ‘a’]
[‘’, 2, ‘ab’]
[‘’, 2, ‘abc’]
[‘abcabc’]
[‘abcabc’, 3]
[‘abcabc’, 3, ‘’]
[‘abcabc’, 3, ‘c’]
[‘abcabc’, 3, ‘cd’]
[‘abcabccdcdcd’]
[‘abcabccdcdcde’]
[‘abcabccdcdcdef’]
''' ‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’
