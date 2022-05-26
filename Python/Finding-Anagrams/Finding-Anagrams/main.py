# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
import re

def main_word(my_word):
    #removing spacing
    word = my_word.replace(" ", "")
    #removes all punctation marks and symbols using regular expression
    my_string = re.sub(r'[^\w\s]', '', word)
    #change all words to lowercase
    my_string = my_string.lower()
    return my_string


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = main_word(word)
    anagram = main_word(anagram)
    if sorted(word) == sorted(anagram):
        return True
    return False

#Sample Test Cases
print (find_anagram("hello", "check"))
print(find_anagram("Heavy rain", "Hire a navy"))
print (find_anagram("To be or not to be: that is the question, whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune.",
"In one of the Bard's best-thought-of tragedies, our insistent hero, Hamlet, queries on two fronts about how life turns rotten."))
