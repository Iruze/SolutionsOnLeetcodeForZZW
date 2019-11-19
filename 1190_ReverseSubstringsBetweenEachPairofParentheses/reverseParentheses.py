class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = ['']
        for me in s:
            if me == '(':
                res.append('')
            elif 'a' <= me and me <= 'z':
                res[-1] += me
            else:
                tmp = res.pop()
                res[-1] += tmp[::-1]
        return res[0]
        
        
''' '''''''''''''''''''''''''''''''''''''''''''''''''''
# 输入样例
a(bcdefghijkl(mno)p)q

  ['']
a ['a']
( ['a', '']
b ['a', 'b']
c ['a', 'bc']
d ['a', 'bcd']
e ['a', 'bcde']
f ['a', 'bcdef']
g ['a', 'bcdefg']
h ['a', 'bcdefgh']
i ['a', 'bcdefghi']
j ['a', 'bcdefghij']
k ['a', 'bcdefghijk']
l ['a', 'bcdefghijkl']
( ['a', 'bcdefghijkl', '']
m ['a', 'bcdefghijkl', 'm']
n ['a', 'bcdefghijkl', 'mn']
o ['a', 'bcdefghijkl', 'mno']
) ['a', 'bcdefghijklonm']
p ['a', 'bcdefghijklonmp']
) ['apmnolkjihgfedcb']
q ['apmnolkjihgfedcbq']
''' '''''''''''''''''''''''''''''''''''''''''''''''''''
