import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | Det N PP
VP -> V NP | V NP PP
PP -> P NP
Det -> 'the' | 'a'
N -> 'dog' | 'cat' | 'park' | 'man'
V -> 'saw' | 'chased'
P -> 'in' | 'with'
""")

sentence = "the dog chased the cat in the park".split()

parser = nltk.RecursiveDescentParser(grammar)

print("Sentence:", ' '.join(sentence))
print("Top-Down Parse Trees:")
for tree in parser.parse(sentence):
    print(tree)
