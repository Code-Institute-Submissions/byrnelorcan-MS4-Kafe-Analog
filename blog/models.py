from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=254)
    blog_content = models.TextField()
    blog_id = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.blog_title
