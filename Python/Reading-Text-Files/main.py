# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#Method to remove punctuation marks and \n from file
def remove_punc(word):
    punc = '''!()-[]{};:'"\n,<>./?@#$%^&*_~'''
    nopunc = ""
    for ele in word:
        if ele not in punc:
            nopunc = nopunc + ele
    return nopunc


#Method to read file and create a list of all words in the text
def read_file_content(file_doc):
    final = [] 
    f = open(file_doc, "r")
    sentences = f.read()
    words = sentences.split(" ")
    for each_word in words:
        res = remove_punc(each_word)
        final.append(res)
    f.close()
    return final


#This method uses a hashmap to count the occurence of words in the file
def count_words(text):
    # [assignment] Add your code here
    total = dict()
    for word in text:
        word = word.lower() #convert to lowercase
        if word in total:
            total[word] += 1
        else:
            total[word] = 1
    return total

main_text = read_file_content("Reading-Text-Files\story.txt")
print (count_words(main_text))   
