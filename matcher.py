# matcher.py
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def rank_resumes(job_desc, resumes):
    texts = [job_desc] + resumes
    preprocessed = [preprocess(text) for text in texts]

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(preprocessed)
    scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    return scores
