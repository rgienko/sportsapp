import datetime

from django.shortcuts import render
import requests
from datetime import date, timedelta
import pytz
from tzlocal import get_localzone


# Create your views here.
def home(request):
    url = "https://livescore6.p.rapidapi.com/news/v2/list"

    headers = {
        'x-rapidapi-host': "livescore6.p.rapidapi.com",
        'x-rapidapi-key': "6b8f9cbcb4msh4fd25bb1e095b9fp1695fcjsnc47ff00d6bac"
    }

    response = requests.request("GET", url, headers=headers).json()

    return render(request, '../templates/layout.html')


def hockey(request):
    live_hockey_scores_url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

    headers = {
        'x-rapidapi-host': "livescore6.p.rapidapi.com",
        'x-rapidapi-key': "6b8f9cbcb4msh4fd25bb1e095b9fp1695fcjsnc47ff00d6bac"
    }

    return render(request, '../templates/hockey.html')


def getScoresByDate(sport, dte):
    import requests

    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"

    querystring = {"Category": sport, "Date": dte}

    headers = {
        'x-rapidapi-host': "livescore6.p.rapidapi.com",
        'x-rapidapi-key': "6b8f9cbcb4msh4fd25bb1e095b9fp1695fcjsnc47ff00d6bac"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    my_dict = {}
    response = response['Stages']
    for stage in response:
        key = stage['Sdn']
        try:
            my_dict[key].append(stage['Stages'])
        except KeyError:
            my_dict = {**my_dict, **{key: stage['Events']}}

    return my_dict
