def prime_number(n):
    if n <= 1:
        print("Prime number")
    else:
        prime = True

        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                prime = False
                break
        print(prime)


n = int(input("Enter the number to check: "))
prime_number(n)
