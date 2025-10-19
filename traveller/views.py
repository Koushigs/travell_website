from django.shortcuts import render
from .models import Destination


# Create your views here.
def index(request):
    
    return render(request, "index.html", ) 

def travel_destination(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.img = 'trip/1.png'
    dest1.prise = 700
    dest1.desc = 'The place there is no Night'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Bengalore'
    dest2.img = 'trip/2.png'
    dest2.prise = 750
    dest2.desc = 'The silicion city'
    dest2.offer = True

    dest3 = Destination()
    dest3.name ='Bangkok'
    dest3.img = 'trip/3.png'
    dest3.prise = 800
    dest3.desc ='The beautifull night life ever'
    dest3.offer = False

    dests =[dest1 , dest2, dest3]
    return render(request, "travel_destination.html", {'dests' : dests}, )


def contact(request):
    return render(request, "contact.html")

