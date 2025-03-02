import joblib

# ✅ Model aur Vectorizer Load Karna
model = joblib.load("fake_comment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")  # Agar training me use kiya tha

# ✅ Test Data
test_comments = [
    "This is a genuine product review.",  # Expected: Real
    "Congratulations! You won a free iPhone!",  # Expected: Fake
    "I highly recommend this book to everyone.",  # Expected: Real
    "Claim your lottery prize now!",  # Expected: Fake
]

# ✅ Model Se Predict Karna
for comment in test_comments:
    transformed_comment = vectorizer.transform([comment])  # ✅ Ensure transformation
    prediction = model.predict(transformed_comment)[0]
    result = "Fake" if prediction == 1 else "Real"
    print(f"Comment: {comment} → Prediction: {result}")
