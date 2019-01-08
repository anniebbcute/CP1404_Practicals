
words = input("Enter a sentence: ").split()
words.sort()
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
for key, value in word_to_count.items():
    print(key," : ", value)