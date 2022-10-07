from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Share(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    body= models.TextField()
    image = models.ImageField(upload_to="image/" , blank=True, null=True)
    created_on= models.DateTimeField(auto_now_add=True)
    image =models.ImageField(null=True, blank=True)
    author =models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("share_list")

# Create your models here.
    # def get_absolute_url(self):
    #     return reverse("share_list", args=[self.id])