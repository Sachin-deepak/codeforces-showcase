def solve(n, k, s):
    chars = sorted(set(s))
    if k > n:
        print(s + chars[0] * (k - n))
        return
    s = list(s[:k])
    for i in range(k-1, -1, -1):
        for c in chars:
            if c > s[i]:
                s[i] = c
                for j in range(i+1, k):
                    s[j] = chars[0]
                print(''.join(s))
                return
    print(''.join(s))

n, k = map(int, input().split())
s = input()
solve(n, k, s)