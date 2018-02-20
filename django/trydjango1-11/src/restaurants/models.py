from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

from .validators import validate_category


class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name


def restaurant_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving...')
    if not instance.slug:
        slug = slugify(instance.name)  # change the attibute to the field that would be used as a slug
        new_slug = slug
        count = 0
        while instance.__class__.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
            count += 1
            new_slug = '{slug}-{count}'.format(slug=slug, count=count)

        instance.slug = new_slug


def restaurant_post_save_receiver(sender, instance, created, *args, **kwargs):
    print('saved')
    print(instance.timestamp)


pre_save.connect(restaurant_pre_save_receiver, sender=Restaurant)
post_save.connect(restaurant_pre_save_receiver, sender=Restaurant)
