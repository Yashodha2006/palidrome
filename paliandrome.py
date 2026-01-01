import sys

# Check if input is given through command line
if len(sys.argv) > 1:
    word = sys.argv[1]
else:
    word = input("Enter a word: ")

# Convert to lowercase for accurate comparison
word = word.lower()

# Reverse the word
rev = word[::-1]

# Check palindrome
if word == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
