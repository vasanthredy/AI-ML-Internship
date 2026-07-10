import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("sentiment.csv")

X = data["text"]
y = data["sentiment"]

# Convert text to vectors
vectorizer = TfidfVectorizer(stop_words="english")
X_vector = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vector, y)

# Save model
joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Sentiment Analysis Model Trained Successfully!")