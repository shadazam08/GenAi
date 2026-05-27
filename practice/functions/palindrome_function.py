def palindrome(word):
    # toLower = word 
    toLower = word.lower()
    reverseWord = toLower[::-1]
    if(toLower == reverseWord):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")

# Example usage
inputWord = input("Enter a word: ")
palindrome(inputWord)