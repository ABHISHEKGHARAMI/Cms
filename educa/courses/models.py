from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


# Model for the Subjects

class Subject(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150,unique=True)
    
    class Meta:
        ordering = ['title']
        
        
    # str method
    def __str__(self):
        return self.title
    
    
    
# model for the course

class Course(models.Model):
    owner = models.ForeignKey(User,
                              related_name='course_created',
                              on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150,unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    
    # meta class
    class Meta:
        ordering = ['-created']
        
        
    # str method
    def __str__(self):
        return self.title
    
    
# class for the module
class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    
    # str method
    def __str__(self):
        return self.title
    
# class for the Content

class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type','object_id')
    
