# Day 04 – Python Strings

## Topics Learned

### 1. String Fundamentals
- What is a string?
- Creating strings using single and double quotes.
- Difference between integers and numeric strings.

### 2. String Indexing
- Positive indexing
- Negative indexing
- Accessing individual characters
- Spaces are also characters.

### 3. String Slicing
Syntax:
```python
string[start:end:step]
```
- Start index is included.
- End index is excluded.
- Step controls the movement between characters.
- Reverse a string using `[::-1]`.

### 4. String Immutability
Python strings are immutable. Individual characters cannot be modified directly after creation.

A new string can be created using slicing and concatenation.

### 5. String Methods

| Method | Purpose |
|---|---|
| `upper()` | Converts to uppercase |
| `lower()` | Converts to lowercase |
| `title()` | Capitalizes each word |
| `capitalize()` | Capitalizes the first character |
| `strip()` | Removes whitespace from both ends |
| `lstrip()` | Removes whitespace from the left |
| `rstrip()` | Removes whitespace from the right |
| `replace()` | Replaces specified text |
| `find()` | Finds the position of a substring; returns -1 if absent |
| `index()` | Finds a substring; raises ValueError if absent |
| `count()` | Counts occurrences |
| `split()` | Converts a string into a list |
| `join()` | Joins strings using a separator |
| `startswith()` | Checks the beginning of a string |
| `endswith()` | Checks the ending of a string |
| `isdigit()` | Checks whether characters are digits |
| `isalpha()` | Checks whether characters are alphabetic |
| `isalnum()` | Checks for letters and digits |

### 6. String Formatting
- f-strings
- `.format()`
- Positional placeholders
- Named placeholders

### 7. String Operations
- Concatenation using `+`
- Repetition using `*`
- Membership using `in` and `not in`

### 8. Escape Characters

| Escape | Purpose |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

## Practical Exercises Completed

1. Basic string operations and length.
2. Reverse a string using slicing.
3. Check whether a word is a palindrome.
4. Count occurrences of a character.
5. Count words in a sentence.
6. Remove spaces from a sentence.
7. Count vowels using a loop and membership checking.
8. Check whether a string contains only digits.
9. Convert a sentence into a hyphen-separated string using `split()` and `join()`.
10. Check whether a filename has a PDF extension.

## Important Concepts Learned

- Strings are immutable.
- Python indexing starts at zero.
- Negative indexing starts from the end.
- Slicing excludes the ending index.
- `find()` and `index()` have different not-found behaviour.
- `split()` converts a string into a list.
- `join()` combines strings using a separator.
- String methods usually return a new value rather than modifying the original string.

## Interview Questions Practised

1. What is a string in Python?
2. What is the difference between indexing and slicing?
3. Why are strings immutable?
4. What is the difference between `split()` and `join()`?
5. What is the difference between `find()` and `index()`?
6. What is an f-string?
7. What are membership operators?

## What I Learned

Today I learned how to work with strings in Python, access individual characters, extract substrings, manipulate text using built-in methods and solve practical string problems.

I also practised explaining Python concepts in an interview-style format.

## Day Status

**Completed ✅**

Day 04 – Python Strings