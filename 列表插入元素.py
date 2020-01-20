a = 'abcdefgh'


def insert_str(x: str, position: int, value: str):
    if position > len(x):
        raise KeyError
    else:
        new_str = x[:position] + value + x[position:]
    return new_str


print(insert_str(a, 3, '1111'))
"""
abc1111defgh
"""
'haha'