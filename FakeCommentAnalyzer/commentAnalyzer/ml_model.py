import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# ✅ Step 1: Dataset Load Karo
df = pd.read_csv("../FakeCommentAnalyzer/fake_reviews.csv")  # Ensure correct path

# ✅ Step 2: Correct Columns Use Karo
X = df['text_']   # Input Text
y = df['label'].map({'CG': 1, 'OR': 0})  # Fake = 1, Real = 0

# ✅ Step 3: Train-Test Split (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # ✨ Ye line missing thi!

# ✅ Step 4: TF-IDF + Naive Bayes Model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# ✅ Step 5: Model Train Karo
model.fit(X_train, y_train)

# ✅ Step 6: Accuracy Check Karo
accuracy = model.score(X_test, y_test)
print(f"✅ Model Training Complete! Accuracy: {accuracy:.2f}")

# ✅ Step 7: Model Save Karo
joblib.dump(model, "../fake_comment_model.pkl")
print("✅ Model Saved as 'fake_comment_model.pkl'")
z