from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()

    return HttpResponse(
        f"""
        <h1>Welcom to GoBackend !</h1>
        <p>There is my favorites bands</p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
            <li>{bands[3].name}</li>
        </ul>
        """
    )

def about(request):
    return HttpResponse(
        """
        <h1>About Us</h1>
        <p>We revolutionize backend developement</p>
        """
    )

def listings(request):
    listings = Listing.objects.all()

    return HttpResponse (
        f"""
        <h1>Listings</h1>
        <p>Here our awesome collection</p>
        <ul>
            <li>{listings[0].title}</il>
            <li>{listings[1].title}</il>
            <li>{listings[2].title}</il>
            <li>{listings[3].title}</il>
        </ul>
        """
    )

def contact(request):
    return HttpResponse (
        """
        <h1>Contact Us</h1>
        <p>Reach us out at</p>
        """
    )

