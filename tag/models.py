from django.db import models

from place.models import BaseModelPlace


class Tag(BaseModelPlace):
    name = models.CharField('Tag name', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fp_tag'
