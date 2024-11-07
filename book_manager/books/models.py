from django.db import models
class BookInfo(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField()
    author = models.CharField(max_length=300)
    Language = models.CharField(max_length=300)
    Summary = models.TextField(default="No summary available")
    cover = models.ImageField(upload_to='images/', null=True)
# Create your models here.
