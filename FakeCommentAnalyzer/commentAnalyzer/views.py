from django.shortcuts import render
import joblib
import os
from .models import AnalyzedComment




import matplotlib.pyplot as plt
import io
import urllib
import base64
from django.shortcuts import render
from .models import AnalyzedComment





from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AnalyzedComment

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    return render(request, "commentAnalyzer/index.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # User ko direct login karwa dena
            return redirect("analyze")
    else:
        form = UserCreationForm()
    return render(request, "commentAnalyzer/signup.html", {"form": form})



@login_required
def history(request):
    user_history = AnalyzedComment.objects.all().order_by("-created_at")  # ✅ Ensure data fetch ho raha ho
    return render(request, "commentAnalyzer/history.html", {"history": user_history})











def stats(request):
    fake_count = AnalyzedComment.objects.filter(result="Fake").count()
    real_count = AnalyzedComment.objects.filter(result="Real").count()

    # Pie Chart Banana
    labels = ["Fake Comments", "Real Comments"]
    sizes = [fake_count, real_count]
    colors = ["red", "green"]
    explode = (0.1, 0)

    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, explode=explode, shadow=True, startangle=140)
    plt.axis("equal")

    # Image Encode Karna
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request, "stats.html", {"chart": uri})




# ✅ Model ka sahi path set karna
model_path = os.path.join(os.path.dirname(__file__), 'fake_comment_model.pkl')

if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Error: Model file not found at: {model_path}")

# ✅ Model ko load karna
model = joblib.load(model_path)

def analyze_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        prediction = model.predict([comment])  # Model se prediction lena
        result = "Fake" if prediction[0] == 1 else "Real"

        AnalyzedComment.objects.create(text=comment, result=result)

        return render(request, 'commentAnalyzer/result.html', {'comment': comment, 'result': result})  # ⚠️ Path check karna

    return render(request, 'analyze.html')  # ⚠️ Path check karna
