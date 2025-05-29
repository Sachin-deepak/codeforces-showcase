def solve(n, k, s):
    ch = sorted(set(s))
    if k > n:
        return s + ch[0] * (k - n)
    s = list(s[:k])
    
    for i in range(k-1, -1, -1):
        for j in ch:
            if j > s[i]:
                s[i] = j
                s[i+1:k] = ch[0] * (k - i - 1)
                return ''.join(s)
    return ''.join(s)

n, k = map(int, input().split())
s = input()
print(solve(n, k, s))
