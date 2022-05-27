# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here

    lines = [] 
    # set the file "story.txt" to open and close automatically
    with open('story.txt') as file:
        # read the text file line by line and return as string
        lines = file.readlines()
    # set line count
    count = 0
    # for each line in lines of the file
    for line in lines:
        # increment the line by one
        count += 1
        # print line count and contents in each line
        print(f'line {count}: {line}')
    return "Hello World"
print(read_file_content([]))

def count_words(line):
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    word_count = {}
    with open("./story.txt", "r") as fi:
        for line in fi:
            words = line.split()
            for word in words:
                word = word.upper
                if word not in word_count:
                    word_count[word] = 0
            word_count[word] += 1
        list(word_count.keys())[:30]
    no_of_words = list(word_count.keys())[:30]
    for word in no_of_words:
        #print(word_count[word])
        return {"as": 10, "would": 20}
    print("{0:15}{1:2d}".format(word, word_count[word]))
print(count_words([]))


