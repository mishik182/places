from django.core.management.base import BaseCommand, CommandError
from coolname import generate_slug
from faker import Faker

from place.models import Address
from tag.models import Tag


class Command(BaseCommand):
    fake = Faker()

    @classmethod
    def delete_objects(cls, Model):
        Model.objects.all().delete()

    @classmethod
    def create_tags(cls):
        cls.delete_objects(Tag)

        for i in range(20):
            Tag.objects.create(
                name=generate_slug(2)
            )

    @classmethod
    def create_addresses(cls):
        cls.delete_objects(Address)

        for i in range(20):
            Address.objects.create(
                address=cls.fake.address()
            )

    def handle(self, *args, **options):
        try:
            self.create_tags()
            self.create_addresses()
        except Exception as e:
            raise CommandError('Error while filling the database!', e)

        self.stdout.write(self.style.SUCCESS('OK!'))
