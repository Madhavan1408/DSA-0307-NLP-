from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Natural language processing helps computers understand human language",
    "Machine learning is a subset of artificial intelligence",
    "Deep learning models are used in natural language processing tasks",
    "Artificial intelligence includes machine learning and natural language processing"
]

query = "natural language processing and machine learning"

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform([query])

scores = cosine_similarity(query_vector, tfidf_matrix).flatten()
ranked_indices = scores.argsort()[::-1]

print("Query:", query)
print("\nDocument Ranking:")
for rank, idx in enumerate(ranked_indices, 1):
    print(f"Rank {rank}: Doc {idx+1} (score={scores[idx]:.4f}) -> {documents[idx]}")
