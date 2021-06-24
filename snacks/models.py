from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.urls.base import reverse

# Create your models here.


class Snack(models.Model):
    title = models.CharField(max_length=256)
    purchaser = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse("snack_detail", args=[str(self.id)])