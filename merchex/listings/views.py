from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse(
        "<h1>Welcom to GoBackend !</h1>"
    )

def about(request):
    return HttpResponse(
        """
        <h1>About Us</h1>
        <p>We revolutionize backend developement</p>
        """
    )

def listings(request):
    return HttpResponse (
        """
        <h1>Listings</h1>
        <p>Here our awesome collection</p>
        """
    )

def contact(request):
    return HttpResponse (
        """
        <h1>Contact Us</h1>
        <p>Reach us out at</p>
        """
    )

