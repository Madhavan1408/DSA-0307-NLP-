import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'boy' | 'ball'
V -> 'kicked'
""")

sentence = "the boy kicked the ball".split()
parser = nltk.ChartParser(grammar)

print("Sentence:", ' '.join(sentence))
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
