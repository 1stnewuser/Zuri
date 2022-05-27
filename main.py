# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    word = "good"
    anagram = "doog"
     
# Check if both string are of the same length
    if(len(word) == len(anagram)):

        #sort both string 
        str1_anagram = sorted(word)
        str2_anagram = sorted(anagram)

        # If sorted char arreyers are same
        if(str1_anagram == str2_anagram):
            return True        
        else:
            print(word + " and " + anagram + " are not anagrams. ")
    print("Pass")
print(find_anagram("good", "doog"))


