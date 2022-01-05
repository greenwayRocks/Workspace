from django.shortcuts import render, get_object_or_404

from .choices import price_choices, bedroom_choices, state_choices
from .models import Listing


def index(request):
    listings = Listing.objects.all().filter(is_published=True)

    context = {
        'listings': listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    query_listings = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_listings = query_listings.filter(
                description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_listings = query_listings.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_listings = query_listings.filter(state__iexact=state)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_listings = query_listings.filter(bedrooms__lte=bedrooms)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_listings = query_listings.filter(price__lte=price)

    context = {
        'listings': query_listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
