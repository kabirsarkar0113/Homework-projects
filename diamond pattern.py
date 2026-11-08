n = 5  # number of rows in the top half (the widest row is the middle)

# Top half (including the middle row)
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Bottom half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))