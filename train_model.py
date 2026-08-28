import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

MODEL_FILE = "fake_news_model.pkl"
VECTORIZER_FILE = "tfidf_vectorizer.pkl"

def train():
    print("⏳ Downloading realistic dataset for training...")
    
    # Using a reliable public CSV with verified labels
    dataset_url = "https://raw.githubusercontent.com/joolsa/fake_news_detector/master/data/fake_or_real_news.csv"
    df = pd.read_csv(dataset_url)

    # Clean missing values
    df = df.dropna(subset=['text', 'label'])

    # Map labels: REAL -> True, FAKE -> False
    df['label'] = df['label'].apply(lambda x: True if str(x).strip().upper() == 'REAL' else False)

    print(f"📊 Dataset loaded: {len(df)} total records ({df['label'].sum()} Real, {len(df) - df['label'].sum()} Fake)")

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        df['text'], df['label'], test_size=0.2, random_state=42
    )

    # Extract features using TF-IDF
    print("⚙️ Vectorizing text data...")
    vectorizer = TfidfVectorizer(
        stop_words='english',
        max_df=0.75,
        min_df=3,
        ngram_range=(1, 2),
        max_features=10000
    )
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Train Classifier
    print("🧠 Training PassiveAggressiveClassifier...")
    model = PassiveAggressiveClassifier(max_iter=100, random_state=42, C=0.5)
    model.fit(X_train_tfidf, y_train)

    # Evaluate
    y_pred = model.predict(X_test_tfidf)
    acc = accuracy_score(y_test, y_pred)
    print(f"🎯 Test Accuracy: {acc * 100:.2f}%")

    # Save artifacts
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)

    with open(VECTORIZER_FILE, "wb") as f:
        pickle.dump(vectorizer, f)

    print("✅ Model & Vectorizer updated and saved!")

if __name__ == "__main__":
    train()
