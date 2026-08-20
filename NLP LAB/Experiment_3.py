import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

text = "The children were playing happily and studying various interesting stories"
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("Tokens:", tokens)
print("POS Tags:", tags)
print(f"{'Word':<12}{'Stem':<12}{'Lemma':<12}")
for word in tokens:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word, pos='v')
    print(f"{word:<12}{stem:<12}{lemma:<12}")
