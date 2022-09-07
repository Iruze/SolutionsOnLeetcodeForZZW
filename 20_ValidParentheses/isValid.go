func isValid(s string) bool {
    n := len(s)
    // 奇数数量的必然不能“配对”
    if n & 1 == 1 {
        return false
    }

    stack := []byte{}
    pair := map[byte]byte{
        '(': ')',
        '[': ']', 
        '{': '}',
    }

    for i := 0; i < n; i++ {
        // 注意byte的类型初零值是0，可以和0比较，其他类型则不行，比如string的初零值是""
        if len(stack) == 0 || pair[s[i]] != 0 {
            stack = append(stack, s[i])
        } else if s[i] == pair[stack[len(stack) - 1]] {
            // 弹出“成对”的括号
            stack = stack[:len(stack) - 1]
        } else {
            return false
        }
    }

    return len(stack) == 0
}
