from django.shortcuts import render
import urllib.request
from bs4 import BeautifulSoup

def index(request, platform, btag):

    # css,
    #  check Makkukurīmī#1513 btag
    # 500 if no endorce at all

    if platform not in ['pc', 'psn', 'xbl']:
        return notFound(request)

    urlopen = urllib.request.urlopen('https://playoverwatch.com/pl-pl/career/' + platform + '/' + btag)

    soup = BeautifulSoup(urlopen, 'html.parser')


    isOK = soup.find('div', attrs={'class':'u-center'})
    if isOK is None:
        return render(request, '404.html')

    level = soup.find('div', attrs={'class':'u-center'}).text
    total = soup.find('svg', attrs={'class':'EndorsementIcon-border--shotcaller'})['data-total']
    shotcaller = soup.find('svg', attrs={'class':'EndorsementIcon-border--shotcaller'})['data-value']
    teammate = soup.find('svg', attrs={'class':'EndorsementIcon-border--teammate'})['data-value']
    sportsmanship = soup.find('svg', attrs={'class':'EndorsementIcon-border--sportsmanship'})['data-value']

    endorsement = Endorsement(total, level, shotcaller, sportsmanship, teammate)

    return render(request, 'index.html', {'endorsement': endorsement})

class Endorsement(object):
    total = 0
    level = 0
    shotcaller = 0
    sportsmanship = 0
    teammate = 0

    def __init__(self, total, level, shotcaller, sportsmanship, teammate):
        self.total = total
        self.level = level
        self.shotcaller = shotcaller
        self.sportsmanship = sportsmanship
        self.teammate = teammate

def notFound(request):
    return render(request, '404.html')
