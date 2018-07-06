from django.shortcuts import render
from django.http import HttpResponse
import urllib
from bs4 import BeautifulSoup

from .models import Greeting

# Create your views here.
def index(request):

    page = urllib.urlopen('https://playoverwatch.com/pl-pl/career/pc/Artysta-2221')
    soup = BeautifulSoup(page, 'html.parser')
    total = soup.find('svg', attrs={'class':'EndorsementIcon-border--shotcaller'})['data-total']
    shootcaller = soup.find('svg', attrs={'class':'EndorsementIcon-border--shotcaller'})['data-value']
    teammate = soup.find('svg', attrs={'class':'EndorsementIcon-border--teammate'})['data-value']
    sportsmanship = soup.find('svg', attrs={'class':'EndorsementIcon-border--sportsmanship'})['data-value']

    print(total)
    return HttpResponse(total)
    # print 'total endorsement is: ' + total
    # print 'shootcaller endorsement is: ' + shootcaller
    # print 'teammate endorsement is: ' + teammate
    # print 'sportsmanship endorsement is: ' + sportsmanship
    # return HttpResponse('Hello from Python!')
    # return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
