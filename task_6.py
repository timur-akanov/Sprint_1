def digit_root(num: int) -> int:
    while num >= 10:
        s = 0
        while num:
            s += num % 10
            num //= 10
        num = s
    return num

print(digit_root(4851))   # 9
print(digit_root(97569))  # 9
print(digit_root(889987)) # 4