from django.db import models

# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'media')
    bio = models.TextField()

class Image(models.Model):
    image = models.ImageField(upload_to = 'media/')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile)
    likes = models.TextField()
    comments = models.TextField()

    # implement methods
