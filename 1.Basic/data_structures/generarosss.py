def count_numbers(n):
    count = 1
    while count <= n:
        yield count
        count += 1


user_input = int(input("Enter the limit number to count: "))

for i in count_numbers(user_input):
    print(i)
