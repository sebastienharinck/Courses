from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.shortcuts import reverse

from .validators import validate_category

User = settings.AUTH_USER_MODEL  # to be sure that we import the last user model


class RestaurantQuerySet(models.query.QuerySet):
    def search(self, query):  # Restaurant.objects.all().search(query) | Restaurant.objects.filter(something).search(query)
        if query:
            query = query.strip()
            return self.filter(
                Q(name__icontains=query)|
                Q(location__icontains=query)|
                Q(category__icontains=query)|
                Q(item__name__icontains=query)|
                Q(item__contents__icontains=query)
            ).distinct()
        return self


class RestaurantManager(models.Manager):
    def get_queryset(self):
        return RestaurantQuerySet(self.model, using=self._db)

    def search(self, query):  # Restaurant.objects.search()
        return self.get_queryset().search(query)


class Restaurant(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, unique=True)

    objects = RestaurantManager() # add Model.objects.all()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurants:detail', args=(self.slug, ))


def restaurant_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving...')
    if not instance.slug:
        slug = slugify(instance.name)  # change the attribute to the field that would be used as a slug
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
