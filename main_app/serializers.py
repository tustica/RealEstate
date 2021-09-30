from rest_framework import serializers
from main_app.models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Listing
        fields=('price', 'address', 'main_pic', 'description', 'beds','bath','square_feet')