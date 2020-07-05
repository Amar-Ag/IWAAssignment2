def is_palindrome(inputWord):
    """
    Create a function, is_palindrome, to determine if a supplied word is
    the same if the letters are reversed.
    """
    reversedInput = inputWord[::-1]
    print(reversedInput)
    if reversedInput.lower() == inputWord.lower():
        return True
    else:
        return False


userInput = str(input("Enter a string:")) or "racecar"
if is_palindrome(userInput):
    print(f"{userInput} is palindrome.")
else:
    print(f"{userInput} is not palindrome.")
