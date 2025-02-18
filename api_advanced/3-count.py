#!/usr/bin/python3
"""
3-main
"""
import sys

if __name__ == '__main__':
    # Import the count_words function from the 3-count.py file
    count_words = __import__('api_advanced.3-count').count_words  # Adjusted to use api_advanced module
    
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        # Call the count_words function with the subreddit and list of keywords
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])

