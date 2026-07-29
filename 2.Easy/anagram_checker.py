def anagram_checker(word1, word2):
    clean1 = word1.replace(" ", "").strip().lower()
    clean2 = word2.replace(" ", "").strip().lower()

    if len(clean1) != len(clean2):
        return False

    return sorted(clean1) == sorted(clean2)


print(anagram_checker("krishna", "anhsirk"))
print(anagram_checker("Listen", "Silent"))
