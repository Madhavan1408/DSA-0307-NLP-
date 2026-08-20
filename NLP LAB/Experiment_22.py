import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

pronouns = {'he', 'she', 'it', 'they', 'him', 'her', 'them'}

def resolve_references(text):
    sentences = nltk.sent_tokenize(text)
    last_entity = None
    resolved = []
    for sent in sentences:
        tokens = nltk.word_tokenize(sent)
        tagged = nltk.pos_tag(tokens)
        new_tokens = []
        for word, tag in tagged:
            if word.lower() in pronouns and last_entity:
                new_tokens.append(f"{word}[{last_entity}]")
            else:
                new_tokens.append(word)
            if tag in ('NNP', 'NN') and word[0].isupper():
                last_entity = word
        resolved.append(' '.join(new_tokens))
    return resolved

text = "Ravi went to the market. He bought some vegetables. Priya called him later. She asked about the vegetables."

resolved_sentences = resolve_references(text)
print("Original text:", text)
print("\nResolved sentences:")
for s in resolved_sentences:
    print(s)
