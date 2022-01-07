import datetime

from django.shortcuts import render
import requests
from datetime import date, timedelta
import pytz
from tzlocal import get_localzone


# Create your views here.

def index(request):
    url = "https://v1.hockey.api-sports.io/"

    payload = {}

    get_what = 'games'
    dt = date.today()
    timezone = get_localzone()

    headers = {
        'x-rapidapi-host': "v1.hockey.api-sports.io",
        'x-rapidapi-key': "8cda7f9e3ef5b2dc538fca8432320b5d"
    }

    response = requests.request("GET", url + get_what + "?date=" + str(dt),
                                headers=headers, data=payload)

    hockey_games = response.json()['response']

    return render(request, '../templates/hockeyv2.html',
                  {
                      'response': response,
                      'hockey_games': hockey_games

                  })


def getTimeZone():
    import http.client

    conn = http.client.HTTPSConnection("v1.hockey.api-sports.io")

    headers = {
        'x-rapidapi-host': "v1.hockey.api-sports.io",
        'x-rapidapi-key': "8cda7f9e3ef5b2dc538fca8432320b5d"
    }

    conn.request("GET", "/timezone", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
