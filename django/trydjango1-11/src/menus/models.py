from django.conf import settings
from django.db import models


from restaurants.models import Restaurant


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(Restaurant)

    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='Seperate each item by comma')
    excludes = models.TextField(blank=True, null=True, help_text='Seperate each item by comma')
    public = models.BooleanField(default=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_contents(self):
        return self.contents.split(',')

    def get_excludes(self):
        return self.excludes.split(',')
