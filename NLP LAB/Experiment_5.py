from nltk.stem import PorterStemmer

words = ["running", "flies", "happiness", "connection", "connected", "connecting",
         "argued", "studies", "national", "generalization", "relational"]

stemmer = PorterStemmer()

print(f"{'Word':<18}{'Stem':<18}")
for word in words:
    print(f"{word:<18}{stemmer.stem(word):<18}")
