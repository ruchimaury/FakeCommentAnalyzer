from django.db import models
from django.contrib.auth.models import User

class CommentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    result = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.comment[:30]}..."




class AnalyzedComment(models.Model):
    text = models.TextField()  # Comment Text
    result = models.CharField(max_length=10)  # Fake ya Real
    created_at = models.DateTimeField(auto_now_add=True)  # Date & Time

    def __str__(self):
        return f"{self.text[:30]}... - {self.result}"


class Comment(models.Model):
    text = models.TextField()
    is_fake = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
