def sum_of_naturals(n):
    ''' first n*(n+1) is calculated the it is floor divided by 2 i.e. //2'''
    return n*(n+1)//2


number = int(input("Enter the number: "))
print(sum_of_naturals(number))
