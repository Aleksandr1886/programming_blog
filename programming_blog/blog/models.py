from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


  class Category(models.Model):
      name = models.CharField(max_length=100)
      slug = models.SlugField(max_length=200, unique=True)

      def __str__(self):
          return self.name