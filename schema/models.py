from django.db import models
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
# transactions
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from datetime import timedelta
import datetime


class Tutor(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    about = models.CharField(max_length=1000, null=True, blank=True)
    photo = models.ImageField(upload_to='profile_pics',
                              blank=True, null=True)
    thumb_photo = models.ImageField(upload_to='profile_pics_thumbs',
                                    blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        old_photo = self.photo.path if self.photo else None
        super().save(*args, **kwargs)
        try:
            if old_photo != self.photo.path:
                with open(self.photo.path, 'rb') as f:
                    self.thumb_photo = SimpleUploadedFile(
                        self.photo.name, f.read())
                super().save()
                img = Image.open(self.thumb_photo.path)
                if img.height > 200 or img.width > 200:
                    output_size = (200, 200)
                    img.thumbnail(output_size)
                    img.save(self.thumb_photo.path)
        except:
            pass


class Course(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tutor = models.ForeignKey(
        Tutor, on_delete=models.DO_NOTHING,  null=True, blank=True)
    photo = models.ImageField(upload_to='profile_pics',
                              blank=True, null=True)
    thumb_photo = models.ImageField(upload_to='profile_pics_thumbs',
                                    blank=True, null=True)
    intro_video_embed_id = models.CharField(
        max_length=25, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        old_photo = self.photo.path if self.photo else None
        super().save(*args, **kwargs)
        try:
            if old_photo != self.photo.path:
                with open(self.photo.path, 'rb') as f:
                    self.thumb_photo = SimpleUploadedFile(
                        self.photo.name, f.read())
                super().save()
                img = Image.open(self.thumb_photo.path)
                if img.height > 200 or img.width > 200:
                    output_size = (200, 200)
                    img.thumbnail(output_size)
                    img.save(self.thumb_photo.path)
        except:
            pass


class Outline(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f'{self.course}: {self.title}'


class Applicant(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    other_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    photo = models.ImageField(upload_to='profile_pics',
                              blank=True, null=True)
    thumb_photo = models.ImageField(upload_to='profile_pics_thumbs',
                                    blank=True, null=True)
    course = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        old_photo = self.photo.path if self.photo else None
        super().save(*args, **kwargs)
        try:
            if old_photo != self.photo.path:
                with open(self.photo.path, 'rb') as f:
                    self.thumb_photo = SimpleUploadedFile(
                        self.photo.name, f.read())
                super().save()
                img = Image.open(self.thumb_photo.path)
                if img.height > 200 or img.width > 200:
                    output_size = (200, 200)
                    img.thumbnail(output_size)
                    img.save(self.thumb_photo.path)
        except:
            pass
