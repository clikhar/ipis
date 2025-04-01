from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name= 'Mumbai'
    dest1.desc = 'City of Dreams'
    dest1.img = 'destination_1.jpg'
    dest1.price = 1000
    dest1.offer =True

    dest2 = Destination()
    dest2.name = 'Nagpur'
    dest2.desc = 'City of Oranges'
    dest2.img = 'destination_2.jpg'
    dest2.price = 2500
    dest2.offer = False

    dests=[dest1,dest2]
    return render(request,'index.html',{'dests':dests})