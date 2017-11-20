from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.

class QuoteManager(models.Manager):
    results = {'errors': []}
    def validate(self, postData):
        if len(postData['person']) < 3:
            results['errors'].append("Must be more than 3 chars")

        if len(postData['message']) < 10:
            results['errors'].append("Quote must be longer than 10 chars")

        return results



class Quote(models.Model):
    name = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='quotes')
    owner = models.ManyToManyField(User, related_name='owners')
    favorite = models.ManyToManyField(User, related_name='favorites')
    objects = QuoteManager()