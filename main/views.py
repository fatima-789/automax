from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Listing, LikedListing
from .forms import ListingForm
from .filters import ListingFilter

from users.forms import LocationForm
from django.contrib import messages

def main_view(request):
    return render(request, 'views/main.html')

@login_required
def home_view(request):
    listings = Listing.objects.all()
    listing_filters = ListingFilter(request.GET, queryset=listings)
    user_like_listings = LikedListing.objects.filter(profile=request.user.profile).values_list('listing')
    like_listings_ids = [l[0] for l in user_like_listings]
    context = {
        'listings' : listings, 
        'listing_filters' : listing_filters,
        'like_listings_ids' : like_listings_ids,
    }
    return render(request, 'views/home.html', context)

def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST)
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.success(request, f'{listing.title} Listing Posted Successfully! ')
                return redirect('home')
            else:
                raise Exception
        except Exception as err:
            print(err)
            messages.error(request, 'An error occured in Listing. Try again later!')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request, 'views/list.html', {'listing_form': listing_form, 'location_form': location_form})

@login_required
def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        return render(request, 'views/listing.html', {'listing' : listing})
    except Exception as e:
        messages.error(request, f'Inavlid UID {id}')
        return redirect('home')

@login_required    
def edit_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        if request.method == 'POST':
            listing_form = ListingForm(request.POST, request.FILES, instance=listing)
            location_form = LocationForm(request.POST, instance=listing.location)
            if listing_form.is_valid() and  location_form.is_valid():       
                listing_form.save()
                location_form.save()
                messages.success(request, 'Updated List Successfully.')
                return redirect('home')
            else:
                raise Exception
        else:
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)
            context = {
                'listing_form': listing_form,
                'location_form': location_form,
            }
    except Exception as e:
        messages.error(request, 'An error occured for editing the book list.')
        return redirect('home')
    print(id)
    return render(request, 'views/edit.html', context)
@login_required
def like_listing_view(request, id):
    listing = get_object_or_404(Listing, id=id)

    liked_listing, created = LikedListing.objects.get_or_create(profile=request.user.profile, listing=listing)

    if not created:
        liked_listing.delete()
    else:
        liked_listing.save()

    return JsonResponse({
        'is_liked_by': created,
    })