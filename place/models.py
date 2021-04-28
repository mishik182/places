from django.db import models
from django.contrib.auth.models import BaseUserManager


class BaseModelPlace(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(BaseModelPlace):
    address = models.CharField('Address string', max_length=128)

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'fp_address'


class PreferManager(BaseUserManager):
    def get_queryset(self):
        return super(PreferManager, self).get_queryset().all().order_by('-is_prefer')


class Place(BaseModelPlace):
    objects = PreferManager()
    name = models.CharField('Place name', max_length=128)
    distance = models.PositiveIntegerField('Distance')
    address = models.ForeignKey(Address, verbose_name='Address', on_delete=models.CASCADE)
    tag = models.ManyToManyField('tag.Tag', verbose_name='Tag')
    is_prefer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fp_place'
