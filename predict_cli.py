import argparse
import joblib
import os
from typing import Tuple

MODEL_PATH = "models/phishing_model.joblib"

def load_model(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Model not found at {path}. Train it first with train_model.py"
        )
    return joblib.load(path)

def classify_probability(prob_phishing: float) -> str:
    if prob_phishing >= 0.85:
        return "Very Suspicious"
    elif prob_phishing >= 0.65:
        return "Suspicious"
    elif prob_phishing >= 0.45:
        return "Uncertain – needs review"
    else:
        return "Likely Safe"

def predict_email(text: str) -> Tuple[str, float]:
    model = load_model(MODEL_PATH)
    proba = model.predict_proba([text])[0]

    classes = list(model.classes_)
    # Our labels are "legit" and "phishing"
    phishing_index = classes.index("phishing")

    prob_phishing = float(proba[phishing_index])
    label = classify_probability(prob_phishing)
    return label, prob_phishing

def main():
    parser = argparse.ArgumentParser(
        description="Simple AI-powered phishing email detector"
    )
    parser.add_argument(
        "--email",
        type=str,
        help="Email text to classify. If omitted, read from stdin."
    )

    args = parser.parse_args()

    if args.email:
        email_text = args.email
    else:
        print("Paste the email text below. Press Ctrl+Z then Enter when done (on Windows):")
        email_text = ""
        try:
            while True:
                line = input()
                email_text += line + "\n"
        except EOFError:
            pass

    label, prob = predict_email(email_text)
    print("\n=== RESULT ===")
    print(f"Verdict: {label}")
    print(f"Probability of phishing: {prob:.2%}")

if __name__ == "__main__":
    main()
