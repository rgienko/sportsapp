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
        'x-rapidapi-key': "6178d2f0b7fc6ce443e3362eb18b9cc8"
    }

    response = requests.request("GET", url+get_what+"?date="+str(dt)+"&timezone="+str(timezone), headers=headers, data=payload)

    hockey_games = response.json()['response']

    return render(request, '../templates/hockeyv2.html',
                  {
                      'response': response,
                      'hockey_games': hockey_games

                  })


