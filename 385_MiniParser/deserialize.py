class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        stack = []
        num, sign, is_num = 0, 1, False
        for i, c in enumerate(s):
            if c == '-':
                sign = -1
            elif c.isdigit():
                num = num * 10 + int(c)
                is_num = True
            elif c == '[':
                stack.append(NestedInteger())
            elif c == ']' or c == ',':
                if is_num:
                    cur_list = stack.pop()
                    cur_list.add(NestedInteger(sign * num))
                    stack.append(cur_list)
                num, sign, is_num = 0, 1, False
                if c == ']' and len(stack) > 1:
                    cur_list = stack.pop()
                    stack[-1].add(cur_list)
        return stack[0]
