#!/usr/bin/env python3

import sys

def count_word():
    """
    Counts the number of occurances of each word in the
    input text file

    Returns a dict with the unique word as the key (str)
    and the number of times it occurs as the value (int)
    """

    word_count_dict = {} 

    for line in sys.stdin: # Read lines from the input

        # Split the line into words by spaces and remove trailing whitespaces (Tokenizing)
        words = line.strip().split() 

        for word in words: # Iterate through the words in the line
            if word in word_count_dict: 
                word_count_dict[word] += 1 # Increment count if the word is already in the dict
            else:
                word_count_dict[word] = 1 # Set count to 1 if the word is not in the dict
    return word_count_dict 


def sort_and_print(word_count_dict):
    """
    Sorts the given dictionary and prints the output
    in the format: word frequency
    """

    sorted_words = sorted(word_count_dict.keys()) 
    for word in sorted_words: # Iterates through the dict 
        frequency = word_count_dict[word]
        print(f"{word} {frequency}")


def main():
    """
    Calls two helper functions: count_word() and
    sort_and_print

    Prints the words and their corresponding frequencies
    """

    word_count_dict = count_word()
    sort_and_print(word_count_dict)

        
if __name__ == "__main__":
    main()
