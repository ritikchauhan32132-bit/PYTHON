user = input("Enter a string: ")

# 1. Original String
print("Original String:", user)

# 2. Length
print("Length:", len(user))

# 3. Uppercase
print("Uppercase:", user.upper())

# 4. Lowercase
print("Lowercase:", user.lower())

# 5. Title Case
print("Title Case:", user.title())

# 6. Capitalize
print("Capitalize:", user.capitalize())

# 7. Swap Case
print("Swap Case:", user.swapcase())

# 8. Reverse String
print("Reverse:", user[::-1])

# 9. First Character
print("First Character:", user[0])

# 10. Last Character
print("Last Character:", user[-1])

# 11. Character Count
ch = input("Enter a character to count: ")
print("Count:", user.count(ch))

# 12. Replace
print("Replace a with @:", user.replace("a", "@"))

# 13. Starts With
print("Starts with P:", user.startswith("P"))

# 14. Ends With
print("Ends with n:", user.endswith("n"))

# 15. Remove Spaces
print("Strip:", user.strip())

# 16. Split
print("Split:", user.split())

# 17. Is Alphabet
print("Is Alphabet:", user.isalpha())

# 18. Is Digit
print("Is Digit:", user.isdigit())

# 19. Is Alphanumeric
print("Is Alphanumeric:", user.isalnum())

# 20. Is Lower
print("Is Lower:", user.islower())

# 21. Is Upper
print("Is Upper:", user.isupper())

# 22. Find
print("Find 'a':", user.find("a"))

# 23. Index
# Agar 'a' na ho to error aayega
# print(user.index("a"))

# 24. Word Count
print("Total Words:", len(user.split()))

# 25. Vowel Count
vowels = "aeiouAEIOU"
count = 0

for i in user:
    if i in vowels:
        count += 1

print("Vowels:", count)

# 26. Palindrome Check
if user == user[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")