import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

def evaluate_coherence(text):
    sentences = nltk.sent_tokenize(text)
    if len(sentences) < 2:
        return 1.0, sentences
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    similarities = []
    for i in range(len(sentences) - 1):
        sim = cosine_similarity(tfidf_matrix[i], tfidf_matrix[i + 1])[0][0]
        similarities.append(sim)
    avg_coherence = sum(similarities) / len(similarities)
    return avg_coherence, similarities

coherent_text = "Natural language processing is a field of artificial intelligence. It focuses on the interaction between computers and human language. NLP techniques are used to analyze and understand text."

incoherent_text = "Natural language processing is a field of artificial intelligence. The weather today is sunny and warm. I like eating pizza on weekends."

for label, text in [("Coherent text", coherent_text), ("Incoherent text", incoherent_text)]:
    score, sims = evaluate_coherence(text)
    print(label + ":", text)
    print("Sentence-pair similarities:", [round(s, 3) for s in sims])
    print("Overall coherence score:", round(score, 3))
    print("-" * 50)
