from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


def train_model(X_train, y_train):
    """
        Train a machine learning model using the provided training data.

        Parameters:
        X_train (array-like): The input features for training.
        y_train (array-like): The target labels for training.

        Returns:
        model: The trained machine learning model.
    """

    # Create a pipeline with TF-IDF vectorizer and Multinomial Naive Bayes classifier
    pipeline = make_pipeline(TfidfVectorizer(), MultinomialNB())
    # Fit the model on the training data
    model = pipeline.fit(X_train, y_train)

    return model
