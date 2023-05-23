# Create your views here.

from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UrlShortenerSerializer
from rest_framework.views import APIView

class UrlShortenerView(APIView):

    @api_view(['POST'])
    def post(request):
        data = request.data
        longurl = data['longurl']
        shorturl = UrlShortenerSerializer.save(longurl)
        shorturl = "http://localhost:8000/"+shorturl
        return Response({'longurl': longurl, 'shorturl': shorturl})


    def get(request, shorturl):
        return redirect(UrlShortenerSerializer.getLongUrl(shorturl))
