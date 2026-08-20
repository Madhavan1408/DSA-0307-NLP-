import random
from collections import defaultdict
import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

random.seed(42)

corpus = """the quick brown fox jumps over the lazy dog the dog barks at the fox
the fox runs into the forest the quick fox is clever the lazy dog sleeps all day"""

tokens = nltk.word_tokenize(corpus.lower())
bigrams = list(nltk.bigrams(tokens))

model = defaultdict(list)
for w1, w2 in bigrams:
    model[w1].append(w2)

def generate_text(start_word, num_words=10):
    word = start_word
    result = [word]
    for _ in range(num_words - 1):
        if word not in model:
            break
        word = random.choice(model[word])
        result.append(word)
    return ' '.join(result)

print("Bigram model built from corpus.")
print("Generated text (start='the'):", generate_text("the", 12))
print("Generated text (start='fox'):", generate_text("fox", 10))
