### filter函数

> 验证 "A man, a plan, a canal: Panama" 是否为回文串，仅考虑字母&数字，不考虑大小写

```python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [*filter(str.isalnum, s.lower())]
        return s == s[::-1]
```

filter的用法：
> `filter()`也接收一个函数和一个序列。`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。

* `s.lower()`可作用于字符串s中的每一个字符
* `str.isalnum` 判断字符是字母或者数字字符
* `*`用来解包，这里作用跟`list()`一样

```python3
>>> s
'A man, a plan, a canal: Panama'
>>> s.lower()
'a man, a plan, a canal: panama'
>>> str.isalnum('a')
True
>>> t = map(int, ['2', '3', '4'])
>>> t
<map object at 0x106fa98e0>
>>> [*t]
[2, 3, 4]
```
