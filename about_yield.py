def plus_one_iter(x):
    for i in range(x):
        yield i + 1


print(sum(plus_one_iter(10)))
"""
55
"""

print(list(plus_one_iter(10)))
"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
