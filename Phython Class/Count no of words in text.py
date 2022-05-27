#Select text file to open in read mode
file = open("Zuri count num in text.txt","r")
#Set count to zero
count = 0
#For every word in a line
for line in file:
    #seperate the words by spaces into a list
    words = line.split(" ")
    #count and increment the word
count += len(words)
file.close()
print("Number of words in text file:", count)
