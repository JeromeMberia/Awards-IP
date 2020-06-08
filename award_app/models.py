from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rate(models.Model):
    rater = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey('app.Project',on_delete=models.CASCADE,related_name='rates')
    design = models.PositiveIntegerField(default=0)
    usability = models.PositiveIntegerField(default=0)
    content = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.rater.username
