from prime_library import factor
from itertools import count
from collections import Counter


cycle_length = {}
for d in range(2, 1001):
    factors = factor(d)
    factors |= {2: 0, 5: 0}
    del factors[2], factors[5]
    d_prime = factors.product()
    if d_prime == 1:
        cycle_length[d] = 0
        continue
    # print(f"going into test loop on {d=}")
    for k in count(1):
        if (10**k - 1) % d_prime == 0:
            cycle_length[d] = k
            break
    # print(f"{d_prime=}")
print(cycle_length)
print(Counter(cycle_length).most_common())

