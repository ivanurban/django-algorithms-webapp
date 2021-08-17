from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.






class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


            


class Post(models.Model):
        STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
        DIFFICULTY_LEVEL_CHOICES = [
        ('easy','Easy'),
        ('medium','Medium'),
        ('hard','Hard'),
        ]
        title = models.CharField(max_length=250)
        
        slug = models.SlugField(max_length=250,unique_for_date='publish')
        author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
        body = models.TextField()
        task_link = models.URLField(max_length=200, blank=True)
        body_code = models.TextField(blank=True)
        publish = models.DateTimeField(default=timezone.now)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')
        difficulty = models.CharField(max_length=6,choices=DIFFICULTY_LEVEL_CHOICES, default='easy')

        class Meta:
            ordering = ('-publish',)


        def __str__(self):
            return self.title

        def get_absolute_url(self):
            return reverse('algoblog:post_detail',args=[self.publish.year,self.publish.month, self.publish.day, self.slug])
            #return reverse('algoblog:post_detail',args=[self.slug])



        objects = models.Manager() # The default manager.
        published = PublishedManager() # Our custom manager.
            

