L = [x * x for x in range(10)]
print(L)

m = (x * x for x in range(10))
print(m)

for n in m:
    print(n)
