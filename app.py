import streamlit as st
import joblib
import os

MODEL_PATH = "models/phishing_model.joblib"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model not found at {MODEL_PATH}. Train it first with train_model.py"
        )
    return joblib.load(MODEL_PATH)

def classify_probability(prob_phishing: float) -> str:
    if prob_phishing >= 0.85:
        return "Very Suspicious"
    elif prob_phishing >= 0.65:
        return "Suspicious"
    elif prob_phishing >= 0.45:
        return "Uncertain – needs review"
    else:
        return "Likely Safe"

def main():
    st.title("🛡️ AI-Powered Phishing Email Detector")
    st.write("Paste an email below and I'll estimate whether it looks like phishing.")

    email_text = st.text_area(
        "Email text",
        height=250,
        placeholder="Paste the full email (subject + body) here..."
    )

    if st.button("Analyze"):
        if not email_text.strip():
            st.warning("Please paste an email first.")
            return

        model = load_model()
        proba = model.predict_proba([email_text])[0]
        classes = list(model.classes_)
        phishing_index = classes.index("phishing")
        prob_phishing = float(proba[phishing_index])
        verdict = classify_probability(prob_phishing)

        st.subheader("Result")
        st.write(f"**Verdict:** {verdict}")
        st.write(f"**Probability of phishing:** `{prob_phishing:.2%}`")

        st.progress(min(max(prob_phishing, 0.0), 1.0))

        if verdict.startswith("Very") or verdict.startswith("Suspicious"):
            st.error("Be careful – this email looks risky.")
        elif verdict.startswith("Likely Safe"):
            st.success("This email looks mostly safe, but always double-check sensitive links.")
        else:
            st.info("The model is unsure. Manually review this email.")

if __name__ == "__main__":
    main()
