from django.contrib import admin
from .models import Comment
from .models import AnalyzedComment


@admin.register(AnalyzedComment)
class AnalyzedCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'result', 'created_at')  # Admin Panel Me Yeh Columns Dikhne Chahiy

admin.site.register(Comment)  # 👈 Comment model ko admin panel me dikhane ke liye
