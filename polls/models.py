from django.db import models


# Create your models here.

class userss(models.Model):
    name = models.TextField(max_length=100, blank=False,)

    def __str__(self):
        return self.name


class zone(models.Model):
    user = models.ForeignKey(userss,on_delete=models.CASCADE)
    description = models.TextField(max_length=150, blank=False)
    agreement_template=models.TextField(max_length=100, blank=False)

