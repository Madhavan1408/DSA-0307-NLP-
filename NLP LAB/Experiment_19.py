import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

sentences = [
    "I went to the bank to deposit money",
    "He sat on the bank of the river"
]

for sentence in sentences:
    tokens = word_tokenize(sentence)
    sense = lesk(tokens, 'bank')
    print("Sentence:", sentence)
    if sense:
        print("Best sense for 'bank':", sense.name())
        print("Definition:", sense.definition())
    else:
        print("No sense found")
    print("-" * 50)
