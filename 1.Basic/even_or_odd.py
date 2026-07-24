def even_or_odd(n):
    if n % 2 == 0:
        return f"{n} is an even number"
    elif n % 2 != 0:
        return f"{n} is an odd number"
    else:
        return "Invalid number"


n = float(input("Enter a number: "))
print(even_or_odd(n))

# if __name__ == "__main__":
#     n = 5
#     if even_or_odd(n):
#         print("True")
#     else:
#         print("False")
