from sentence_transformers import SentenceTransformer
import db_connection

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "Artificial Intelligence is the future.",
    "Machine Learning is a subset of AI.",
    "I love playing football."
]


embeddings = model.encode(sentences)

conn = db_connection.conn

# Display embeddings
def createEmbeddings(i, param, embedding):
    pass


for i, embedding in enumerate(embeddings):
    createEmbeddings(i,sentences[i], embedding)
    print(f"Sentence: {sentences[i]}")
    print(f"Embedding: {embedding}...\n")