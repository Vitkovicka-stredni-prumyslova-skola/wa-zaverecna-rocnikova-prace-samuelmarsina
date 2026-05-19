def soucet_delitelu(n):
    soucet = 0

    for i in range(1, n):
        if n % i == 0:
            soucet += i

    return soucet

for n in range(1, 10000):
    m = soucet_delitelu(n)

    if soucet_delitelu(m) == n and n != m:

        if n < m:
            print(n, m)