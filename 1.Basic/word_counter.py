def word_and_character_counter(user_inp):
    words_count = len(user_inp.split())
    char_count = len(user_inp)
    char_no_space = len(user_inp.replace(" ", ""))

    print(f"Number of words: {words_count}")
    print(f"Number of characters (space included): {char_count}")
    print(f"Number of characters (no space): {char_no_space}")


user_inp = input("Enter the sentence: ").strip()
word_and_character_counter(user_inp)
