from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=80)
    date_posted = models.DateField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
