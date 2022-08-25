from django.db import models
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#User = get_user_model()

# class Message(models.Model):
#     author = models.ForeignKey(User, related_name='author_messages',on_delete=models.CASCADE)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.author.username
    
#     def last_10_messages(self):
#         return Message.objects.order_by('timestamp').all()[:10]


class Chat(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey('ChatRoom', on_delete=models.CASCADE)

    # def last_10_messages(self):
    #     return Chat.objects.order_by('timestamp').all()[:10]


class ChatRoom(models.Model):
    name = models.CharField(max_length=255)