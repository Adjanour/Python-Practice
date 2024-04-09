def is_palindrome(word: str) -> bool:
    """Checks if a word is a palindrome using a loop for reversal.

    Args:
        word: The word to check.

    Returns:
        True if the word is a palindrome, False otherwise.
    """
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word  

    return word.lower() == reversed_word.lower()

# Example usage (without input)
word = "racecar"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

