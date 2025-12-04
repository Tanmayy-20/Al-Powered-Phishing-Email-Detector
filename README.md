
# 🛡️ AI Powered Phishing Email Detector

A lightweight machine-learning tool that detects whether an email message is **phishing** or **legit**, using Python, TF-IDF feature extraction, and Logistic Regression. Includes a **CLI tool** and **Streamlit Web UI** for easy interaction.

---

## 🚀 Features
- ML-Based phishing detection
- Simple command-line interface
- Web UI powered by Streamlit
- Shows probability/confidence score
- Lightweight (no GPU required)

---

## 🧠 How It Works
1. A dataset of phishing and legitimate emails is prepared.
2. Email text is converted to numerical vector form using **TF-IDF**.
3. A **Logistic Regression** model is trained.
4. The model is saved and used for predictions.
5. Output is classified as:
   - Likely Safe
   - Uncertain – needs review
   - Suspicious
   - Very Suspicious

---

## 📦 Project Structure
AI Powered Phishing Email Detector/
│
├─ data/
│   └─ emails.csv                # dataset
│
├─ models/
│   └─ phishing_model.joblib     # saved model
│
├─ train_model.py                # trains the model
├─ predict_cli.py                # CLI detection tool
└─ app.py                        # Streamlit web UI

---

## ⚙️ Installation

### 1️⃣ Clone or Download Project
git clone <repo-url>
cd AI Powered Phishing Email Detector

### 2️⃣ Create Virtual Environment (Windows)
python -m venv .venv
.venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install scikit-learn pandas joblib streamlit

---

## 📊 Train the Model
python train_model.py

This creates:
models/phishing_model.joblib

---

## 🔍 Run the CLI Tool

### Quick One-line test:
python predict_cli.py --email "Your account has been blocked click here to verify"

### Paste multi-line email:
python predict_cli.py
Paste text → Press Ctrl + Z then Enter

---

## 🌐 Run Web UI (Streamlit)
streamlit run app.py

The app will open at:
➡ http://localhost:8501/

---

## 🧪 Sample Output
=== RESULT ===
Verdict: Very Suspicious
Probability of phishing: 91.42%

---

## 🛠 Tech Stack
| Component | Technology |
|----------|------------|
| Language | Python |
| Libraries | Scikit-Learn, Pandas, Joblib, Streamlit |
| Algorithm | Logistic Regression |
| Text Processing | TF-IDF |

---

## 📌 Future Enhancements
- Train on a larger dataset
- Add metadata features (link count, domain checks)
- LLM-based explanation mode
- Deploy online (Render / Streamlit Cloud)

---

## 🏁 Conclusion
This project demonstrates how machine learning can assist in identifying phishing emails with minimal computational resources. It forms a strong foundation for more advanced AI-based cybersecurity solutions.
