#Steps
#Remove punctuations
#Open the txt file
#Read each line using for loop
#Count the words in a line using the split and len function
#Print output

import string
print(string.punctuation)

#string.punctuation contains all punctuations
#and this function will convert it to "nothing"

def strip_punctuations(line):
    for character in string.punctuation:
        line = line.replace(character, "")
        return line

filepath = "../pyton CLASS/Zuri count num in text.txt"
#creat a new dictionary called word_count
word_count = {}

with open(filepath, 'r') as fi:

    for line in fi:
        #Remove the punctuation
        line = strip_punctuations(line)
        #seperate the words by spaces into a list
        words = line.split()
        #for each word in words
        for word in words:
            #convert to lower case
            word = word.upper()
            #And check if its not in our dictionary
            if word not in word_count:
                #if not create a new entry for it
                word_count[word] = 0
            #Then increment its count by one
            word_count[word] += 1
#print(word_count[word])
#list keys in no particular order
list(word_count.keys())[:50]
#Travers the words and print their count
ten_words = list(word_count.keys())[:50]
for word in ten_words:
    #words musttake up a minimal 15 spaces; and count can take a minimum of 2
    print("{0:15}{1:2d}".format(word, word_count[word]))

