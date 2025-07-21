from sklearn.feature_extraction .text import TfidfVectorizer

docs = [
    "Python is easy",
    "Python is powerful",
    "C++ is fast"
]

vectorizer = TfidfVectorizer()
result = vectorizer.fit_transform(docs)

print(vectorizer.get_feature_names_out())
print(result.toarray())