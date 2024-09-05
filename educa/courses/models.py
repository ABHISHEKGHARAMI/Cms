from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from embed_video.fields import EmbedVideoField
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
    students = models.ManyToManyField(User,
                                      related_name = 'courses_joined',
                                      blank=True)
    
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
    order = OrderField(blank=True, for_fields=['course'])
    
    class Meta:
        ordering = ['order']
    
    # str method
    def __str__(self):
        return f'{self.order}. {self.title}'
    
# class for the Content

class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={
                                         'model__in': (
                                             'text',
                                             'video',
                                             'image',
                                             'file'   
                                         )
                                     })
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type','object_id')
    order = OrderField(blank=True, for_fields=['module'])
    
    class Meta:
        ordering = ['order']
    
    
# applying the content for the different types for the image, mp3, video etc
class ItemBase(models.Model):
    owner = models.ForeignKey(User,
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.title
    
    # for rendering purpose of the content
    def render(self):
        return render_to_string(
            f'courses/content/{self._meta.model_name}.html',
            {'item': self})
    
class Text(ItemBase):
    content = models.TextField()
    
class File(ItemBase):
    content = models.FileField(upload_to='files')
    
class Image(ItemBase):
    content = models.FileField(upload_to='images')
    
class Video(ItemBase):
    content = EmbedVideoField()
    
    
    
    
