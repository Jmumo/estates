from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices,prices_choices
# Create your views here.
def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context={
        'listings':listings,
        'bedrooms':bedroom_choices,
        'price':prices_choices,
    }
    return render(request, 'pages/index.html',context )

def about(request):

    realtors = Realtor.objects.all()
      
    SOM = Realtor.objects.all().filter(is_mvp=True) 

    context = { 
        'realtors':realtors,
        'SOM':SOM
    }

    return render(request, 'pages/about.html',context )   
