import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

def extract_noun_phrases(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
    chunk_parser = nltk.RegexpParser(grammar)
    tree = chunk_parser.parse(tagged)
    noun_phrases = []
    for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
        phrase = ' '.join(word for word, tag in subtree.leaves())
        noun_phrases.append(phrase)
    return noun_phrases

sentence = "The quick brown fox chased the small white rabbit into the deep dark forest"

phrases = extract_noun_phrases(sentence)
print("Sentence:", sentence)
print("Extracted Noun Phrases and meanings:")
for phrase in phrases:
    print(f"- '{phrase}' refers to an entity described by: {phrase}")
