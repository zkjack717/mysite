from django.db import models
from read_statistics.models import ReadNumExpend, ReadDetail
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Blog(models.Model, ReadNumExpend):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Blog: %s>' % self.title

    class Meta:
        ordering = ['-created_time']


# class ReadNum(models.Model):
#     blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
#     read_num = models.IntegerField(default=0)

