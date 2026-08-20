from nltk.corpus import wordnet as wn

word = "bank"

synsets = wn.synsets(word)

print(f"Word: {word}")
print(f"Number of synsets: {len(synsets)}\n")

for syn in synsets[:5]:
    print("Synset:", syn.name())
    print("Definition:", syn.definition())
    print("Examples:", syn.examples())
    print("Lemmas:", [lemma.name() for lemma in syn.lemmas()])
    hypernyms = syn.hypernyms()
    print("Hypernyms:", [h.name() for h in hypernyms])
    print("-" * 50)

dog_syn = wn.synset('dog.n.01')
cat_syn = wn.synset('cat.n.01')
print("Similarity between dog and cat:", dog_syn.wup_similarity(cat_syn))
