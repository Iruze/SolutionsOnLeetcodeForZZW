**必须背诵一些短小精悍、实用价值高的模板，这样才能在解题时候快速突击，举重若轻**

### No1. 两个数组中的最小差值
```python3
arr1.sort()
arr2.sort()
idx1, idx2 = 0, 0
ans = float('Inf')
while idx1 < len(arr1) and idx2 < len(arr2):
    ans = min(ans, abs(arr1[idx1] - arr2[idx2]))
    
    if arr1[idx1] < arr2[idx2]:
        idx1 += 1
    elif arr1[idx1] > arr2[idx2]:
        idx2 += 1
    else:
        return 0
```
