from django.db import models
#from videofield.models import VideoField
# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='images/')
    body = models.TextField(default='')
    pub_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title  # to show the exact title of each model saved otherwise it will show only object 1 etc

    def summary(self):
        return self.body[:100] # to show only 100 caracters of the body text os change it on your html

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y') # abbrievation of the month name and %e is for the day
