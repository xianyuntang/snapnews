from django.db import models


# Create your models here.

class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=50, unique=bool, null=False)
    name = models.CharField(max_length=20, null=False)
    enable = models.BooleanField(null=False)

    def __str__(self):
        return f"{self.name} | 啟用: {int(self.enable)}"
