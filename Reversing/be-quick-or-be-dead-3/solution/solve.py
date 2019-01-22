#!/usr/bin/python
n = 0x186b5

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

def calc(n):
    if (n <= 0x4):
        x = n * n + 0x2345
    else:
        x = calc(n - 0x5) * 0x1234 + (calc(n - 0x1) - calc(n - 0x2)) + (calc(n - 0x3) - calc(n - 0x4));
    return x

calc = memoize(calc)

# Prevent from recursion error
for i in range(n):
	calc(i)

print calc(n) & (2 ** 64 - 1)
