import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

text = "Natural language processing enables computers to understand human language effectively"

tokens = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)

print("Sentence:", text)
print("Tokens:", tokens)
print("POS Tags:")
for word, tag in pos_tags:
    print(f"{word:<15}{tag}")
