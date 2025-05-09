from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def extract_bow_features(texts):
    vectorizer = CountVectorizer()
    return vectorizer.fit_transform(texts)

def extract_tfidf_features(texts):
    vectorizer = TfidfVectorizer()
    return vectorizer.fit_transform(texts)
