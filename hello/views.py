from django.shortcuts import render
import urllib.request
from bs4 import BeautifulSoup

def index(request):

    page = urllib.request.urlopen('https://playoverwatch.com/pl-pl/career/pc/Artysta-2221')
    soup = BeautifulSoup(page, 'html.parser')
    total = soup.find('svg', attrs={'class':'EndorsementIcon-border--shotcaller'})['data-total']
    shootcaller = soup.find('svg', attrs={'class':'EndorsementIcon-border--shotcaller'})['data-value']
    teammate = soup.find('svg', attrs={'class':'EndorsementIcon-border--teammate'})['data-value']
    sportsmanship = soup.find('svg', attrs={'class':'EndorsementIcon-border--sportsmanship'})['data-value']

    endorsement = Endorsement(total, shootcaller, teammate, sportsmanship)
    return render(request, 'index.html', {'endorsement': endorsement}, {'request': request.build_absolute_uri()})

class Endorsement(object):
    total = 0
    shootcaller = 0
    sportsmanship = 0
    teammate = 0

    def __init__(self, total, shootcaller, sportsmanship, teammate):
        self.total = total
        self.shootcaller = shootcaller
        self.sportsmanship = sportsmanship
        self.teammate = teammate
