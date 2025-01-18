# Given a string paragraph and a string array of the banned words banned, return the most frequent word 
# that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]

# paragraph = "a, a, a, a, b,b,b,c, c"
# banned = ["a"]

paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]

import re
word_count = {}
para = re.sub(r'[^a-zA-Z]', ' ', paragraph)
para = para.split(" ")
print(para)
for word in para:
    lower_word = word.lower()
    if lower_word not in banned:
        if lower_word in word_count:
            word_count[lower_word] += 1
        else:
            word_count[lower_word] = 1
            
max_word = ""
max_count = -999
for word,count in word_count.items():
    if count>max_count and word != '':
        max_count = count
        max_word = word
        
print(max_word)
print(word_count)