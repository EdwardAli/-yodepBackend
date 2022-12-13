from turtle import title
from django.db import models
from embed_video.fields import EmbedVideoField
from datetime import datetime

# models.

# testimonial

class Testimonial(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to = 'files/testimonial',blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.name
# project
class Project(models.Model):
    pname = models.CharField(max_length=250, null=False, blank=False)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to ='files/project',blank=True, null=True)
    pdescription = models.TextField()

    def __str__(self):
        return self.pname

# career
class Career(models.Model):
    fullName = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(max_length=254)
    phyAddress = models.CharField(max_length=250)
    attachedFile = models.FileField(upload_to='files/career', max_length=254)

    def __str__(self):
        return self.fullName

# gallary
class Gallary(models.Model):
    date = models.DateField(auto_now=True)
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to='files/gallary', blank=True, null=True)

    def __str__(self):
        return self.location

# News
class News(models.Model):
    newsTitle = models.CharField(max_length=250, null=False, blank=False)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to ='files/news',blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.newsTitle

# Events
class Events(models.Model):
    eventTitle = models.CharField(max_length=250, null=False, blank=False)
    date = models.DateField(auto_now=True)
    videoUrl = EmbedVideoField(blank=True, null=True) 
    body = models.TextField()

    def __str__(self):
        return self.eventTitle

# blog
class Blog(models.Model):
    blogTitle = models.CharField(max_length=250, null=False, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to = 'files/blog', blank=True, null=True)
    subTitle = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.blogTitle

# comment  
class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

# partner  
class Partner(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to = 'files/partner', blank=True, null=True)
    location = models.TextField()

    def __str__(self):
       return self.name

# vacancy
class Vacancy(models.Model):
    position = models.CharField(max_length=250, null=False, blank=False)
    position_summary = models.CharField(max_length=300, null=False, blank=False)
    duties = models.CharField(max_length=500, null=False, blank=False)
    education = models.CharField(max_length=300, null=False, blank=False)
    method_of_application = models.CharField(max_length=300, null=False, blank=False)
    closing_date = models.DateField()

    def __str__(self):
        return self.position