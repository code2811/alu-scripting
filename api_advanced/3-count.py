#!/usr/bin/python3
"""
3-main
"""
import sys

if __name__ == '__main__':
    count_words = __import__('api_advanced.3-count').count_words  # Import count_words from 3-count.py
    
    # Ensure proper usage of the script
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        # Call the function with the subreddit and word list
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])

