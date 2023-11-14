from django.db import models


# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)

    class Meta:
        db_table = 'articles'

    def __str__(self):
        return f"Id: {self.id} {self.name}"

    def __repr__(self):
        return self.name
