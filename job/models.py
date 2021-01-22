from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=290)

    def __str__(self):
        return self.summary  # to show the exact title of each model saved otherwise it will show only object 1 etc