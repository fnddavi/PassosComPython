vogals = "aeiouAEIOU"
phrase = input("Enter a phrase: ")
count = 0
for char in phrase:
    if char in vogals:
        count += 1
print(f"Number of vowels in the phrase: {count}")
