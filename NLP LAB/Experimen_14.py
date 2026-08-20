import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP_sg VP_sg | NP_pl VP_pl
NP_sg -> Det N_sg
NP_pl -> Det N_pl
VP_sg -> V_sg NP
VP_pl -> V_pl NP
NP -> Det N_sg | Det N_pl
Det -> 'the' | 'a'
N_sg -> 'boy' | 'dog'
N_pl -> 'boys' | 'dogs'
V_sg -> 'chases' | 'likes'
V_pl -> 'chase' | 'like'
""")

parser = nltk.ChartParser(grammar)

def check_agreement(sentence):
    tokens = sentence.split()
    trees = list(parser.parse(tokens))
    return len(trees) > 0

test_sentences = [
    "the boy chases the dogs",
    "the boys chase the dog",
    "the boy chase the dog",
    "the boys chases the dog"
]

for s in test_sentences:
    result = check_agreement(s)
    print(f"'{s}' -> {'Grammatically agrees' if result else 'Agreement error'}")
