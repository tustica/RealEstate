from django.db import models

class Listing(models.Model):
    price = models.IntegerField(),
    address = models.CharField(max_length=255)
    main_pic = models.ImageField()
    description = models.TextField()
    beds = models.IntegerField()
    bath = models.IntegerField()
    square_feet = models.IntegerField()
