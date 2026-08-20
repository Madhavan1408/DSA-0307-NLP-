import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | Det N PP
VP -> V NP | V NP PP
PP -> P NP
Det -> 'the' | 'a'
N -> 'dog' | 'cat' | 'telescope' | 'man'
V -> 'saw'
P -> 'with'
""")

sentence = "the man saw a dog with a telescope".split()

earley_parser = nltk.EarleyChartParser(grammar)

print("Sentence:", ' '.join(sentence))
print("Earley Parse Trees:")
for tree in earley_parser.parse(sentence):
    print(tree)
