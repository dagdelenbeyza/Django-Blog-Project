from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Entry(models.Model):
    entry_title = models.CharField(max_length=200)
    enrty_text = models.TextField()
    entry_created_date = models.DateTimeField(
        default=timezone.now)
    entry_published_date = models.DateTimeField(
        blank=True, null=True)
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Entries"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.entry_title}'


class Contact(models.Model):
    STATUS = (
        (1, 'New'),
        (2, 'Read'),
    )
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, null=True)
    message = models.TextField(max_length=500, null=True)
    status = models.IntegerField(choices=STATUS, default=1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact Form Message"
        verbose_name_plural = "Contact From Messages"
