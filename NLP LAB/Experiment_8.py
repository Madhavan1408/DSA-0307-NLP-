import nltk
from collections import defaultdict, Counter

nltk.download('brown', quiet=True)
nltk.download('universal_tagset', quiet=True)

from nltk.corpus import brown

tagged_sents = brown.tagged_sents(tagset='universal')[:2000]

word_tag_counts = defaultdict(Counter)
for sent in tagged_sents:
    for word, tag in sent:
        word_tag_counts[word.lower()][tag] += 1

def stochastic_tag(word):
    word = word.lower()
    if word in word_tag_counts:
        return word_tag_counts[word].most_common(1)[0][0]
    return 'NOUN'

test_sentence = "The old man saw the ship sail near the bank"
tokens = nltk.word_tokenize(test_sentence)

print("Sentence:", test_sentence)
print("Stochastic POS Tags:")
for word in tokens:
    print(f"{word:<12}{stochastic_tag(word)}")
