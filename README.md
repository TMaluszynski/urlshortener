# urlshortener
Projekt "API w DRF to skracania urli"- coś w rodzaju https://tinyurl.com/app tylko samo API.

Funkcjonalność ma być ekstremalnie minimalistyczna, nie chodzi o dodawanie super features (potraktuj to jako podpowiedź :slightly_smiling_face: tu nie trzeba wiele kodować).

Projekt powinien umożliwiać:

Stworzenie skróconego urla, czyli np. wkładamy `http://example.com/very-very/long/url/even-longer` w zamian dostajemy któtki url wygenerowany przez API, np `http://localhost:8000/shrt/`

Rozwinięcie skróconego urla do oryginalnego, czyli odwrotność poprzedniej operacji.


API:
1. shorten the url:\
POST: \<server ip (e.g. localhost)\>:8000/shorten\
  body: longurl = \<long url\>

response: 200 if successful, 400 if long url is malformed or dead\
  format: JSON\
  {\
    "longurl" = \<long url\>\
    "shorturl" = \<result short url\>\
  }\
  \
  example:\
  {\
    "longurl": "https://docs.djangoproject.com/en/4.2/intro/tutorial01/", \
    "shorturl": "http://localhost:8000/Lkl*4c" \
  }\
  \
2. redirect from short url\
GET: \<short url\>\
 \
response: 302 if short url exists in db, 404 if either not in db or malformed\
  redirect to the corresponding long url\
  \
URLs provided in both cases are validated with standard validators library\
Duplicate entries are avoided by either checking randomized pattern samples (in the case of short url generation) or existence of the long url in the db (in such cases the existing short url is provided)\
\
possible improvements (varying effort):
  * class-based views
  * move tests to a separate folder (depends on convention)
  * more edge-case tests
  * automate testing
  
