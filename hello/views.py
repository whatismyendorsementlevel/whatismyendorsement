from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
from bs4 import BeautifulSoup

from .models import Greeting

def index(request):

    page = urllib.request.urlopen('https://playoverwatch.com/pl-pl/career/pc/Artysta-2221')
    print(page)
    soup = BeautifulSoup(page, 'html.parser')
    total = soup.find('svg', attrs={'class':'EndorsementIcon-border--shotcaller'})['data-total']
    shootcaller = soup.find('svg', attrs={'class':'EndorsementIcon-border--shotcaller'})['data-value']
    teammate = soup.find('svg', attrs={'class':'EndorsementIcon-border--teammate'})['data-value']
    sportsmanship = soup.find('svg', attrs={'class':'EndorsementIcon-border--sportsmanship'})['data-value']

    endorsement = Endorsement(total, shootcaller, teammate, sportsmanship)
    print(endorsement)
    return HttpResponse(endorsement)
    # print 'total endorsement is: ' + total
    # print 'shootcaller endorsement is: ' + shootcaller
    # print 'teammate endorsement is: ' + teammate
    # print 'sportsmanship endorsement is: ' + sportsmanship
    # return HttpResponse('Hello from Python!')
    # return render(request, 'index.html')



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

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
