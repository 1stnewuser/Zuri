
    # program to check if two strings are Anagrams!

    str1 ="Race"
    str2 = "care"
    # convert both the string into lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    # strt the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    # if sorted char arrays are the same
    if (sorted_str1 == sorted_str2):
        print(str1 + "and" + str2 + "are anagram.")
    else:
        print(str1 + "and" + str2 + "are not anagram.")