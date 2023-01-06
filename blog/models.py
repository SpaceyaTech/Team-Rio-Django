
from django.conf import settings
from django.db import models
from accounts.models import *
 
class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    publish_comment = models.BooleanField(default=False)

    def approve(self):
        self.publish_comment = True
        self.save()

    def __str__(self):
        return self.text
