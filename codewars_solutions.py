# Solution: Even or Odd
def even_or_odd(number):
    """Determine if a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Solution: Convert a Number to a String
def number_to_string(num):
    """Convert a number to a string."""
    return str(num)



# Solution: Remove String Spaces
def no_space(x):
    """Remove all spaces from a string."""
    return x.replace(" ", "")


# Solution: Vowel Count
def get_count(sentence):
    """Count the number of vowels in a string."""
    count = 0
    for char in sentence:
        if char in "aeiou":
            count += 1
    return count