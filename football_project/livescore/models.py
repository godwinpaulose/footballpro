from django.db import models

class football(models.Model):
    name=models.CharField(max_length=250)
    disc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='photos')
    def __str__(self):
        return self.name

