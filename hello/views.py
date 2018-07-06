from django.shortcuts import render
import urllib.request
from bs4 import BeautifulSoup
from django.template.context import RequestContext

def index(request, platform, btag):

    # validate platform, return 404 when 404, css, obecne przewitywane progi
    urlopen = urllib.request.urlopen('https://playoverwatch.com/pl-pl/career/' + platform + '/' + btag)
    soup = BeautifulSoup(urlopen, 'html.parser')


    isOK = soup.find('div', attrs={'class':'u-center'})
    if isOK is None:
        return render(request, '404.html')

    level = soup.find('div', attrs={'class':'u-center'}).text
    total = soup.find('svg', attrs={'class':'EndorsementIcon-border--shotcaller'})['data-total']
    shootcaller = soup.find('svg', attrs={'class':'EndorsementIcon-border--shotcaller'})['data-value']
    teammate = soup.find('svg', attrs={'class':'EndorsementIcon-border--teammate'})['data-value']
    sportsmanship = soup.find('svg', attrs={'class':'EndorsementIcon-border--sportsmanship'})['data-value']

    endorsement = Endorsement(total, level, shootcaller, sportsmanship, teammate)
    return render(request, 'index.html', {'endorsement': endorsement}, context_instance=RequestContext(request))

class Endorsement(object):
    total = 0
    level = 0
    shootcaller = 0
    sportsmanship = 0
    teammate = 0

    def __init__(self, total, level, shootcaller, sportsmanship, teammate):
        self.total = total
        self.level = level
        self.shootcaller = shootcaller
        self.sportsmanship = sportsmanship
        self.teammate = teammate

def notFound(request):
    return render(request, '404.html')

