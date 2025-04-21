from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=100, unique=True)

class ChatLog(models.Model):
    chat_id = models.CharField(primary_key=True, max_length=100)
    user_id = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    feedback = models.CharField(
        max_length=10,
        choices=[('good', '좋음'), ('normal', '보통'), ('bad', '나쁨')],
        blank=True,
        null=True
    )
    turn = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
