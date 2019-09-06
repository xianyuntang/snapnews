from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Record(models.Model):
    channel = models.CharField(max_length=20)
    time = models.DateTimeField()
    keyword = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"頻道IP:{self.channel} 時間:{self.time} 關鍵字:{self.keyword}"
