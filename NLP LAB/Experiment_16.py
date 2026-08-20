import spacy

nlp = spacy.load("en_core_web_sm")

text = "Apple Inc. was founded by Steve Jobs in Cupertino, California in 1976. It is now led by Tim Cook and competes with Google and Microsoft."

doc = nlp(text)

print("Text:", text)
print("Named Entities:")
for ent in doc.ents:
    print(f"{ent.text:<20}{ent.label_:<10}{spacy.explain(ent.label_)}")
