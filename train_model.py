import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split

MODEL_FILE = "fake_news_model.pkl"
VECTORIZER_FILE = "tfidf_vectorizer.pkl"

def train():
    # 1. Dataset (True = Real News, False = Fake News)
    # Replace or extend this dictionary with a full CSV via pd.read_csv(...)
    data = {
        "text": [
            # Real News (True)
            "Scientists discover new Earth-like planet with water atmosphere.",
            "Central bank announces a 0.25 percent cut in baseline interest rates.",
            "NASA launches Artemis mission to study the lunar surface.",
            "Global summit reaches agreement on carbon reduction targets for 2030.",
            "Stock markets close higher following technology sector quarterly earnings.",
            "Researchers publish clinical trial findings on new malaria vaccine efficacy.",
            "World Health Organization releases updated international health guidelines.",
            "Electric vehicle adoption grows by twenty percent worldwide year over year.",
            
            # Fake News (False)
            "Breaking: Aliens landed in Washington DC and spoke with government leaders.",
            "Drinking boiled lemon water cures every known disease instantly without medicine.",
            "Secret government chip found inside all common grocery store bananas.",
            "Secret miracle plant burns thirty pounds of belly fat overnight while sleeping.",
            "Billionaire reveals loophole that will make everyone rich in three days.",
            "Ancient pyramids were built by time travelers using anti-gravity lasers.",
            "Scientists confirm the moon is hollow and houses an ancient civilization.",
            "5G towers cause immediate cellular mutations and mind control side effects."
        ],
        "label": [
            True, True, True, True, True, True, True, True,
            False, False, False, False, False, False, False, False
        ]
    }

    df = pd.DataFrame(data)

    # 2. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        df['text'], df['label'], test_size=0.2, random_state=42
    )

    # 3. Vectorization
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7, ngram_range=(1, 2))
    X_train_tfidf = vectorizer.fit_transform(X_train)

    # 4. Model Training
    model = PassiveAggressiveClassifier(max_iter=50, random_state=42)
    model.fit(X_train_tfidf, y_train)

    # 5. Save Artifacts
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)

    with open(VECTORIZER_FILE, "wb") as f:
        pickle.dump(vectorizer, f)

    print(f"✅ Saved {MODEL_FILE} and {VECTORIZER_FILE}")

if __name__ == "__main__":
    train()
