def wordCount(t):

    word_dict = {}

    with open(t, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.split()

            for word in words:
                clean_word = word.strip('.,?!;:"()[]{}').lower()

                if clean_word not in word_dict:
                    word_dict[clean_word] = [line_number]
                else:
                    word_dict[clean_word].append(line_number)

    return word_dict

finalout = wordCount('test.txt')
print(finalout)

# here in the wordCount function i am taking each line from the file and also using enumerate to
# keep track of the line numbers/indexing. Then the words are taken by splitting the line into array of words 
# After this i have used a dictionary that is the best option as we need to check if a specific word is there in a dictionary 
# or not. Also dictionary helps us to keep track of the line number and store the word and line number as a key value pair.
