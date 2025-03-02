# 🚀 Fake Comment Analyzer  

**Fake Comment Analyzer** is an AI-powered web application that analyzes comments and determines whether they are **Fake** or **Real**. This project utilizes a Machine Learning model to differentiate between spam and genuine comments.  

---

## 🔥 Features  
✅ AI-based Fake Comment Detection  
✅ User Authentication (Login/Signup)  
✅ Analyze Comments Without Login  
✅ **History Page** for Logged-in Users  
✅ **Graph & Stats Page** for Fake vs Real Comments  
✅ Fully Responsive UI (Mobile, Tablet, Laptop)  

---

## 📌 Tech Stack  
- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite  
- **Machine Learning Model:** Joblib (Pre-trained Model)  
- **Deployment:** PythonAnywhere  

---

## 🚀 Installation & Setup  
Follow these steps to run the project on your system:  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/ruchimaury/FakeCommentAnalyzer.git
cd FakeCommentAnalyzer



Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

Install Dependencies
pip install -r requirements.txt

 Apply Database Migrations

python manage.py migrate
python manage.py collectstatic


Run the Project

python manage.py runserver

 How It Works?
1️⃣ Visit the Home Page and enter a comment for analysis.
2️⃣ The AI model processes the comment and displays the result: Fake or Real.
3️⃣ If Logged In: The analyzed comments are saved in the user history.
4️⃣ Access the History Page to view previously analyzed comments.
5️⃣ Check the Stats Page for a graph of Fake vs Real comments.
6️⃣ You can log out and log in again to continue using the app.




Live Demo
👉 Live Link (If deployed)

🛠️ Future Enhancements
🔹 Improve Comment Analysis Accuracy
🔹 Add More Graphs & Data Insights
🔹 Support for Multiple Languages

📢 Contribute
Want to improve this project? Feel free to fork & contribute!

git clone https://github.com/ruchimaury/FakeCommentAnalyzer.git





 Made with ❤️ by ruchimaurya



---

### **4️⃣ Commit & Push to GitHub**  
If you are adding the README.md file from your local system, use these Git commands:  

```bash
git add README.md
git commit -m "Added project README"
git push origin main
