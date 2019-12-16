from django.db import models

# Create your models here.

class fb_form(models.Model):
    c_name =models.CharField(max_length=30)
    email = models.EmailField()
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)
    outof=models.FloatField()

    def __str__(self):
        return self.c_name