def palindrome(user_inp):
    reverse_word = user_inp[::-1]

    if user_inp == reverse_word:
        return f"The word {user_inp} is palindrome !"
    else:
        return f"The word {user_inp} is not a palindrome !"


user_inp = input("Enter the word: ")
print(palindrome(user_inp))
