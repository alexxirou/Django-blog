from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle1 = models.CharField(max_length=255 ,blank=True)
    body1 = models.TextField(blank=True)
    subtitle2 = models.CharField(max_length=255, blank=True)
    image1 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
    subtitle3 = models.CharField(max_length=255, blank=True)
    body2 = models.TextField(blank=True)
    subtitle4 = models.CharField(max_length=255, blank=True)
    image2 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
    subtitle5 = models.CharField(max_length=255, blank=True)
    body3 = models.TextField(blank=True)
    subtitle6 = models.CharField(max_length=255, blank=True) 
    image3 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
    subtitle7= models.CharField(max_length=255,blank=True)
    #upload_file = models.FileField(upload_to='files/', max_length=None, blank=True)
    body4 = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)