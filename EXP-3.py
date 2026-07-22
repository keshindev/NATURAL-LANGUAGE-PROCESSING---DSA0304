import nltk
from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# Get input from the user
text = input("Enter words separated by spaces: ")

# Split the sentence into words
words = text.split()

print("\nMorphological Analysis")
print("-" * 30)

# Perform stemming
for word in words:
    stem = ps.stem(word)
    print(f"Original Word : {word}")
    print(f"Stem Word     : {stem}")
    print("-" * 30)