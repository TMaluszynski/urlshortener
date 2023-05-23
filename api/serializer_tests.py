import pytest

from .models import UrlShortenerModel
# Create your tests here.

from .serializer import UrlShortenerSerializer, UrlNotValidError


def test_url_should_throw_UrlNotValidError_in_case_url_is_not_valid(db):
    with pytest.raises(UrlNotValidError):
        UrlShortenerSerializer.save('not a valid url')

def test_url_should_create_short_url_if_url_is_valid(db):
    ret = UrlShortenerSerializer.save("https://www.google.com")
    assert ret is not None and len(ret) is 6

def test_existing_url_should_be_retreived_from_db(db):
    shorturl = 'shrurl'
    longurl = "https://www.google.com"
    UrlShortenerModel.createByUrl(shorturl, longurl)
    ret = UrlShortenerSerializer.getLongUrl(shorturl)
    assert ret == longurl

def test_existing_url_should_not_create_a_copy_in_db_and_should_be_retreived(db):
    shorturl = 'shrurl'
    longurl = "https://www.google.com"
    UrlShortenerModel.createByUrl(shorturl, longurl)
    shortret = UrlShortenerSerializer.save(longurl)
    longret = UrlShortenerSerializer.getLongUrl(shorturl)
    assert longret == longurl and shortret == shorturl and UrlShortenerModel.objects.count() is 1
