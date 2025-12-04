import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

DATA_PATH = "data/emails.csv"
MODEL_PATH = "models/phishing_model.joblib"

def load_data(path: str):
    df = pd.read_csv(path)
    # Ensure correct columns and remove missing
    df = df.dropna(subset=["text", "label"])
    return df["text"], df["label"]

def build_pipeline():
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            stop_words="english",
            max_features=5000,
            ngram_range=(1, 2)
        )),
        ("clf", LogisticRegression(
            max_iter=1000,
            n_jobs=-1
        ))
    ])
    return pipeline

def main():
    print("[*] Loading data...")
    X, y = load_data(DATA_PATH)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("[*] Building model...")
    model = build_pipeline()

    print("[*] Training model...")
    model.fit(X_train, y_train)

    print("[*] Evaluating...")
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"[*] Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
