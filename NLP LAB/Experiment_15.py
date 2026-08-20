import nltk
from nltk import PCFG

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | Det N PP [0.4]
VP -> V NP [0.7] | V NP PP [0.3]
PP -> P NP [1.0]
Det -> 'the' [0.6] | 'a' [0.4]
N -> 'man' [0.3] | 'dog' [0.3] | 'park' [0.2] | 'telescope' [0.2]
V -> 'saw' [1.0]
P -> 'with' [0.5] | 'in' [0.5]
""")

sentence = "the man saw a dog with a telescope".split()
viterbi_parser = nltk.ViterbiParser(grammar)

print("Sentence:", ' '.join(sentence))
for tree in viterbi_parser.parse(sentence):
    print(tree)
