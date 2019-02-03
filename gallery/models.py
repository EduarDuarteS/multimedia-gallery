from django.db import models
from django.forms import ModelForm


# Create your models here.

# User model
class User(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'lastName', 'photo', 'city', 'country', 'email', 'password']


# Category model
class Category(models.Model):
    name = models.CharField(max_length=100, null=False)


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


# Multimedia model
class Multimedia(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    creationDate = models.CharField(max_length=20, null=True)
    idCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    typeID = models.CharField(max_length=1000)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return Multimedia


class MultimediaForm(ModelForm):
    class Meta:
        model = Multimedia
        fields = ['title', 'author', 'userId', 'creationDate', 'idCategory', 'typeID', 'city', 'country', 'url']


class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return 'Image: ' + self.name


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'url', 'description', 'type']


# Comment model
class Comment(models.Model):
    comment = models.CharField(max_length=300, null=False)
    userId = models.CharField(max_length=100, null=False)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'userId']


# Clip model
class Clip(models.Model):
    name = models.CharField(max_length=200)
    initialSec = models.SmallIntegerField(default=0)
    finalSec = models.SmallIntegerField(default=0)
    userId = models.CharField(max_length=100, null=False)


class ClipForm(ModelForm):
    class Meta:
        model = Clip
        fields = ['name', 'initialSec', 'finalSec', 'userId']
