"""
get a string and count the occurrences of words in this string
"""
"""
Word Occurrences
Estimate: 30 minutes
Actual:   60  minutes
"""
word_to_count = {}
TEXT = "this is a collection of words of nice words this is a fun thing it is"
# Text = input("enter your text： ")
words = TEXT.split()
for word in words:  # version 1
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
# for word in words:  # version 2
#     word_to_count[word] = word_to_count.get(word, 0) + 1
word_length = max(len(word) for word in words)
for word, count in sorted(word_to_count.items()):
    print(f"{word:{word_length}} :{count}")
