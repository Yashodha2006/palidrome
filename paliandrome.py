import sys

if len(sys.argv) > 1:
    word = sys.argv[1]
else:
    
    word = input("Enter a word: ")

rev = word[::-1]

if word == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
 