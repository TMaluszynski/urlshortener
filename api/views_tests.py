import pytest
from .models import UrlShortenerModel
from .serializer import ShortUrlDoesNotExistError


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

def test_post_should_return_400_when_url_invalid(api_client, db):
    longurl = 'not a valid url'
    response = api_client.post('/shorten', {'longurl': longurl}, format='json')
    assert response.status_code == 400

def test_post_should_return_200_when_url_valid(api_client, db):
    longurl = "https://www.google.com"
    response = api_client.post('/shorten', {'longurl': longurl}, format='json')
    assert response.status_code == 200 and \
           response.json().get('longurl') == longurl and \
           len(response.json().get('shorturl')) is len('http://localhost:8000/')+6

def test_get_should_return_404_when_short_url_not_in_db(api_client, db):
    with pytest.raises(ShortUrlDoesNotExistError):
        shorturl = 'shrurl'
        response = api_client.get('/'+shorturl)
        assert response.status_code == 404

def test_get_should_return_200_and_redirect_when_url_in_db(api_client, db):
    shorturl = 'shrurl'
    longurl = "https://www.google.com"
    UrlShortenerModel.objects.create(shorturl=shorturl, longurl=longurl)
    response = api_client.get('/'+shorturl)
    assert response.status_code == 302 and \
           response['Location'] == longurl