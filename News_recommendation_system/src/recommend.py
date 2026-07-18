import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_article(query):
    """
    It takes the user input query and then recommend based on the cosine similarity.
    """

    data = pd.read_csv("../data/bbc_news_dataset.csv")
    X = data["Text"]

    # Using TfidfVectorizer to convert the text into numbers . if fit_transform is directly used it gives sparse matrix.

    vectorizer = TfidfVectorizer(stop_words="english")
    vectorizer_matrix = vectorizer.fit_transform(X)

    # now get the data from the user and check the similarity score and return that score to the frontend.

    query_vector = vectorizer.transform([query])
    similarity = cosine_similarity(query_vector, vectorizer_matrix)

    # based on the similairity we sort the data and return the 3 similar values.

    indices = similarity.argsort()[0][::-1][1:4]

    similar_data = X.iloc[indices]

    list_similar_data = similar_data.tolist()

    return list_similar_data
