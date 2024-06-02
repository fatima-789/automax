from django.db import models
import uuid
from users.models import Profile, Location
from .consts import BOOK_CATEGORIES, BOOK_CONDITION
from .utils import user_listing_path

class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150, null=False, default=None)
    author = models.CharField(max_length=100, null=False, default=None)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cateogory = models.CharField(max_length=50, choices=BOOK_CATEGORIES, default=None)
    price = models.IntegerField(default=0)
    description = models.TextField()
    condition = models.CharField(max_length=24, choices=BOOK_CONDITION, default=None)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=user_listing_path)

    def __str__(self):
        return f'{self.seller.user.username}\'s Listing - {self.title}'
    
class LikedListing(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.listing.title} is liked by {self.profile.user.username}'