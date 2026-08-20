import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'NN$'),
    (r'.*s$', 'NNS'),
    (r'^(the|a|an)$', 'DT'),
    (r'.*ly$', 'RB'),
    (r'[0-9]+', 'CD'),
    (r'.*', 'NN')
]

regexp_tagger = nltk.RegexpTagger(patterns)

sentence = "The children are playing happily and the dogs barked loudly"
tokens = nltk.word_tokenize(sentence)
tags = regexp_tagger.tag(tokens)

print("Sentence:", sentence)
print("Rule-based POS Tags:")
for word, tag in tags:
    print(f"{word:<12}{tag}")
