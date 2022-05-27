def find_anagrams(string__a, string_b):
    string_a = sorted(string_a)
    string_b = sorted(string_b)
    return string_a == string_b
    print(find_anagrams("t", "Tan"))
    