from django.db import models

# Create your models here.
from setuptools.command.upload import upload


class Room(models.Model):
    # topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = models.
    # image = models.ImageField(null=False, blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Uploads(models.Model):
    myfiles = models.FileField(upload_to="myimages")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    # host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    # description = models.TextField(null=True, blank=True)
    # #participants = models.
    # # image = models.ImageField(null=False, blank=False)
    # updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room


