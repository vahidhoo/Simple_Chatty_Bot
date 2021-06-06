word1 = input()
word2 = input()

# How many letters does the longest word contain?
max_length = len(word1)

if len(word2) > max_length:
    max_length = len(word2)

print(max_length)
