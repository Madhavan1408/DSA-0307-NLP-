import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

sentence = "the race was won by the fast runner who can run fast"
tokens = nltk.word_tokenize(sentence)

initial_tags = ['DT' if w in ('the', 'a', 'an') else 'NN' for w in tokens]

def apply_transformation_rules(words, tags):
    new_tags = tags[:]
    for i in range(len(words)):
        if words[i] == 'run' or words[i] == 'won':
            new_tags[i] = 'VB'
        if i > 0 and new_tags[i - 1] == 'MD' and new_tags[i] == 'NN':
            new_tags[i] = 'VB'
        if words[i] == 'can':
            new_tags[i] = 'MD'
        if words[i] == 'fast':
            new_tags[i] = 'RB' if i > 0 and new_tags[i - 1] in ('VB', 'MD') else 'JJ'
    return new_tags

print("Sentence:", sentence)
print("Initial tags:", list(zip(tokens, initial_tags)))

final_tags = apply_transformation_rules(tokens, initial_tags)
print("After transformation rules:")
for word, tag in zip(tokens, final_tags):
    print(f"{word:<10}{tag}")
