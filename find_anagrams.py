# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(sorted(word)== sorted(anagram)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
    return True

# testing it
word ="listen"
anagram ="silent"
find_anagram(word, anagram)
