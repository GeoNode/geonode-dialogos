from datetime import datetime

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        null=True,
        related_name="comments",
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    content_object = GenericForeignKey()

    comment = models.TextField()

    submit_date = models.DateTimeField(default=datetime.now)
    ip_address = models.GenericIPAddressField(null=True)
    public = models.BooleanField(default=True)

    def __unicode__(self):
        return "pk=%d" % self.pk
