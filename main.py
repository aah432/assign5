memo = []
for i in range(20):
    memo.append(-1)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if ( wt[ n - 1 ] > W ):
        return knapSack(W, wt, val, n - 1)

    else:
        return max(
            val[n - 1] + knapSack(
                W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1))


def maxKnapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


print(fib(6))

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

print(knapSack(W, wt, val, n))
print(maxKnapSack(W, wt, val, n))


def e(s, m, i, j):
    line = ""
    newI = 0
    for i in range(0, m - 1):
        if len(s[i]) + len(line) < m:
            line += s[i] + " "
        else:
            newI = i + 1
            j += 1

    return len(s[newI:j])


def bl(S, M, i, j):

    finishedLine = ""
    LineBadness = 0
    Line = S[i - j]
    for i in range(1, M + 1):
        if len(S[i]) + len(finishedLine) < M:
            finishedLine += S[i] + " "
        else:
            LineBadness += 1

    return LineBadness

def minBad(s, m, i):
    P = [0] * m-1
    C = [0] * m-1

    for i in range (1,m):
        if sum_{i = k}^n l_i + n - k < M
            C[k] = 0
        q = ∞
        for j = 1 to n - k
            cost = sum_{m = 1}^j l_{k + m} + m - 1
            if cost < M and (M - cost)^3 + C[k + m + 1] < q:
                q = (M - cost)^3 + C[k + m + 1]
                P[k] = k + j
        C[k] = q

s = ["aaaaa", "bbbbb", "ccc"]
print(e(s,1,0,2))
print(bl(s,1,0,2))