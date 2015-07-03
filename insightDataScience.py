# Open the file for reading from the directory 'tweets_input'.
with open("tweets_input/tweets.txt", "r") as infile:

    data = infile.read()  # Read the contents of the file into memory.

# Return a list of the lines, breaking at line boundaries.
my_list = data.splitlines()
wordDict = {}             # wordDict is a dictionary for unique words as keys and its number of occurrence as values.
uniqueWords = []          # uniqueWords is a list of integers as number of words in each tweet as its elements.

# Open/Create the file 'ft2.txt' in the 'tweets_output' directory to write in to.
tweetsMedian = open("tweets_output/ft2.txt","w")

for line in my_list:            # Accesses each tweet at a time.
    words = line.split()        # Splits the tweet in separate words.
    numWords = len(words)
    uniqueWords.append(numWords)
    uniqueWords.sort()
    # median is the integer variable to store the latest median value.
    if len(uniqueWords)%2==0:
        median = (uniqueWords[int(len(uniqueWords)/2)]+uniqueWords[int((len(uniqueWords)/2))-1])/2
    else:
        median = uniqueWords[int(((len(uniqueWords)+1)/2))-1]
    # Write the latest modified median value to the 'ft2.txt' file.
    tweetsMedian.writelines(format(median)+'\n')
    for element in words:       # Accesses each word in the list of words in the list
        if element in wordDict.keys():
            wordDict[element]+=1    # if the word already exists in the directory, we increment the value by 1.
        else:
            tempDict={element : 1}
            wordDict.update(tempDict)   # if we come across a new word, we add the word to the dictionary with value 1.
# Open/Create the file 'ft1.txt' in the 'tweets_output' directory to write in to.
tweetsUniqueWordCount = open("tweets_output/ft1.txt", "w")
for keys,values in wordDict.items():
    # Writes the list of unique words with its occurrence in the file from the directory.
    tweetsUniqueWordCount.writelines(keys.ljust(20) + format(values).rjust(10)+'\n')

# Close all the opened files.
tweetsMedian.close()
tweetsUniqueWordCount.close()
infile.close()
