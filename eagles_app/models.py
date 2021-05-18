from django.db import models


# Create your models here.
class Entry(models.Model):
    entry_title = models.CharField(max_length=100)
    entry_body = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.entry_title
