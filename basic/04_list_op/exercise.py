# 4-3
for val in range(1, 21):
    print(val)

# 4-4
arr = list(range(1, 1_000_001))

# 4-3
print(f'min->{min(arr)}')
print(f'max->{max(arr)}')
print(f'sum->{sum(arr)}')

# 4-6
arr = list(range(1, 21, 2))
for val in arr:
    print(val)

# 4-7
arr = list(range(3, 31, 3))
for val in arr:
    print(val)

# 4-8/4-9
arr = [val ** 3 for val in range(1, 11)]
for val in arr:
    print(val)

# 4-10
print(f"the first three items in the list ar: {arr[:3]}")
print(f"three items from the middle of the list are: {arr[4:7]}")
print(f"the last three items in the list are: {arr[-3:]}")

