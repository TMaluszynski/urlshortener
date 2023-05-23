# Create your models here.
from django.db import models
import random


class UrlShortenerModel(models.Model):
    longurl = models.CharField(unique=True, db_index=True, max_length=255)
    shorturl = models.CharField(unique=True, db_index=True, max_length=10)

    def __str__(self):
        return self.shorturl

    @classmethod
    def getByShortUrl(cls, shortUrl):
        return cls.objects.get(shorturl=shortUrl)

    @classmethod
    def getByLongUrl(cls, longUrl):
        return cls.objects.get(longurl=longUrl)

    @classmethod
    def createByUrl(cls, shortUrl, longUrl):
        return cls.objects.create(shorturl=shortUrl, longurl=longUrl)

    @classmethod
    def generateShortUrl(cls):
        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!*^$-_"
        sample = ("".join(random.sample(s, 6)))
        while not UrlShortenerModel.objects.filter(shorturl=sample).exists:
            sample = ("".join(random.sample(s, 6)))
        return sample

