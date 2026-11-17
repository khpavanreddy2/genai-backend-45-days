# Day 04 - Python Strings

# 1. Basic string operations
name = input("Enter your name: ")

print(name.upper())
print(name.lower())
print(name.title())
print(name[0])
print(name[-1])
print(len(name))


# 2. Reverse a string
word = input("Enter a word: ")
print(word[::-1])


# 3. Palindrome checker
word = input("Enter a word: ").lower()

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 4. Character counter
text = input("Enter text: ")
character = input("Enter character: ")

print(text.count(character))


# 5. Word counter
sentence = input("Enter a sentence: ")
words = sentence.split()

print(f"Number of words: {len(words)}")


# 6. Remove spaces
text = "I love Python"
print(text.replace(" ", ""))


# 7. Count vowels
word = input("Enter a word: ").lower()
count = 0

for char in word:
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)


# 8. Check digits
text = input("Enter a string: ")

if text.isdigit():
    print("Only digits")
else:
    print("Not only digits")


# 9. Convert spaces into hyphens
text = "I love Python"
words = text.split()
result = "-".join(words)

print(result)


# 10. Check PDF filename
filename = input("Enter filename: ")

if filename.lower().endswith(".pdf"):
    print("Valid PDF file")
else:
    print("Not a PDF file")