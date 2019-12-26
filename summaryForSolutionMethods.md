### 求两个数的最大公约数
- 欧几里得辗转相除法（递归实现）
```python
def gcd(p, q):
    if q == 0: 
        return p
    return gcd(q, p % q)
```
