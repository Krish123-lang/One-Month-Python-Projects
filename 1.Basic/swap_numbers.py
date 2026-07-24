def swap_numbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return f"{a}, {b}"


print(swap_numbers(10, 90))
