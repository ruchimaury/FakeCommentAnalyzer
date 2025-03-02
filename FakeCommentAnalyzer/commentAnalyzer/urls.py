from django.urls import path
from .views import analyze_comment, history, stats, signup,index
from django.contrib.auth import views as auth_views
urlpatterns = [

    path(",", analyze_comment, name="analyze"),
    path("", index, name="index"),  # ✅ Home page URL
    path('', analyze_comment, name='analyze_comment'),
    path("history/", history, name="history"),
    path("stats/", stats, name="stats"),
    path("signup/", signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="commentAnalyzer/login.html"), name="login"),

    path("logout/", auth_views.LogoutView.as_view(template_name="commentAnalyzer/logout.html"), name="logout"),
]
