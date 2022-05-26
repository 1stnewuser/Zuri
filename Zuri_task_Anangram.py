# declear strings 1,and 2 
str1 = "good"
str2 = "doog"

# Check if both string are of the same length
if(len(str1) == len(str2)):
    
    #sort both string 
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # If sorted char arreyers are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram. ")    
    else:
        print(str1 + " and " + str2 + " are not anagram. ")
else:
    print(str1 + " and " + str2 + " are not anagram. ")


