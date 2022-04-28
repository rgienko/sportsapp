import datetime

from django.shortcuts import render
import requests
from datetime import date, timedelta
import pytz
from tzlocal import get_localzone


# Create your views here.
def get_today_minus_two_days():
    today_minus_two_days = date.today() - timedelta(days=2)
    return today_minus_two_days


def get_today_minus_one_day():
    today_minus_one_day = date.today() - timedelta(days=1)
    return today_minus_one_day


def get_today_plus_two_days():
    today_plus_two_days = date.today() + timedelta(days=2)
    return today_plus_two_days


def get_today_plus_one_day():
    today_plus_one_day = date.today() + timedelta(days=1)
    return today_plus_one_day


def getHockeyScores(dt):
    url = "https://v1.hockey.api-sports.io/"

    payload = {}
    get_what = 'games'
    timezone = get_localzone()

    headers = {
        'x-rapidapi-host': "v1.hockey.api-sports.io",
        'x-rapidapi-key': "8cda7f9e3ef5b2dc538fca8432320b5d"
    }

    response = requests.request("GET", url + get_what + "?date=" + str(dt) + "&timezone=" + str(timezone)
                                + "&league=" + str(57) + "&season=" + str(2021), headers=headers, data=payload)

    hockey_games = response.json()['response']
    return hockey_games


def index(request):
    today = date.today()
    hockey_games = getHockeyScores(today)

    return render(request, '../templates/hockeyv2.html',
                  {
                      'hockey_games': hockey_games,
                      'today': today,
                      'today_m2': get_today_minus_two_days(),
                      'today_m1': get_today_minus_one_day(),
                      'today_p1': get_today_plus_one_day(),
                      'today_p2': get_today_plus_two_days()

                  })
