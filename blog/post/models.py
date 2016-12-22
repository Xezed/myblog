from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = Post.objects.order_by('id')
    if new_id:
        new_id = new_id.last().id + 1
    else:
        new_id = 1
    return '{}{}'.format(new_id, filename)

class Post(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_location, null=True, height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
