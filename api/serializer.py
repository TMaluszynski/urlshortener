import validators
from rest_framework.serializers import ModelSerializer
from .models import UrlShortenerModel
from rest_framework.exceptions import APIException
import validators.url


class UrlNotValidError(APIException):
    status_code = 400
    default_detail = 'provided URL is invalid, please provide a valid URL'
    default_code = 'invalid_url'

class ShortUrlDoesNotExistError(APIException):
    status_code = 404
    default_detail = 'provided short URL does not lead anywhere.'
    default_code = 'dead_url'
class UrlShortenerSerializer(ModelSerializer):
    class Meta:
        model = UrlShortenerModel
        fields = '__all__'

    @classmethod
    def validate(cls, url):
        return validators.url(url)

    @classmethod
    def save(cls, longurl):
        if not UrlShortenerSerializer.validate(longurl):
            raise UrlNotValidError
        try:
            obj = UrlShortenerModel.getByLongUrl(longurl)
        except UrlShortenerModel.DoesNotExist:
            obj = None
        if obj is None:
            shorturl = UrlShortenerModel.generateShortUrl()
            UrlShortenerModel.createByUrl(shorturl, longurl)
        else:
            shorturl = obj.shorturl
        return shorturl

    @classmethod
    def getLongUrl(cls, shorturl):
        try:
            obj = UrlShortenerModel.getByShortUrl(shorturl)
        except UrlShortenerModel.DoesNotExist:
            raise ShortUrlDoesNotExistError

        return obj.longurl
