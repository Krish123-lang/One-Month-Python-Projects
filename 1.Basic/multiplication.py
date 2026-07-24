# for i in range(1, 11):
#     print(f"{5}x{i}={5*i}")


def multiplication(n, limit):
    for i in range(1, limit+1):
        print(f"{n} x {i} = {n*i}")


number = int(input("Enter the number: "))
limit = int(input("Enter the limit: "))
multiplication(number, limit)
