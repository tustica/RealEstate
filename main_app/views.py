from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from main_app.models import Listing
from main_app.serializers import ListingSerializer

def index(request):
    context = {
        'listing': Listing.objects.filter(beds=3)
    }
    return render(request, 'index.html', context)