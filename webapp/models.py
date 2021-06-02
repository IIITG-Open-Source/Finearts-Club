from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="Posts/")
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title

#  Todo : Add year to cordinators


class Coordinator(models.Model):
    name = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to="Profile/")
    from_date = models.DateField()
    to_date = models.DateField()
    gmail = models.CharField(max_length=200, blank=True, null=True)
    insta = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
