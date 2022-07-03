from django.db import models
from django.urls import reverse
# Create your models here.
"""
Notes: For the author key, a ForeignKey allows for a many-to-one relationship meaning that a given user can be the 
author of many blog posts, but not the other way around. All many-to-one relationships such as ForeignKey require an
on_delete option which we must specify.

reverse() allows us to reference an object by its URL template name
"""


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Tells Django how to calculate the canonical URL for our model object. It says use the model post_detail and then
        pass in the primary key
        """
        return reverse('post_detail', kwargs={'pk': self.pk})
