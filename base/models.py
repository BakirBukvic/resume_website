from django.db import models

# Create your models here.


class Link(models.Model):
    url_name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.url_name