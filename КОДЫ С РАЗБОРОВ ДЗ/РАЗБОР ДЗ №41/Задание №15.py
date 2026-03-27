def treug(n, m, k):
    return n + m > k and n + k > m and m + k > n

def f(x):
    return not((treug(x, 11, 18) == (not(max(x, 5) > 68))) and treug(x, A, 5))

for A in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 1000)):
        print(A)