from collections import Counter
from copy import deepcopy
from english_words import english_words_alpha_set as words
# import english_words
# english_words.english_words_alpha_set


all_words = []
l = Counter(input("Words: "))

for word in words:
    if len(word) < 3:
        continue

    all = True
    tmp = deepcopy(l)

    for c in word:
        if c in tmp:
            tmp[c] -= 1
            if tmp[c] < 0:
                all = False
        else:
            all = False

    if all:
        all_words.append(word)

all_words.sort(key=lambda x: -len(x))

print(all_words)