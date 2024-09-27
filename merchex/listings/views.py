from idlelib.rpc import response_queue

from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.core.mail import send_mail

from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm, BandForm, ListingForm


def band_list(request):
    bands = Band.objects.all()

    return render(request,
                  'listings/band_list.html',
                  {
                      "bands": bands,
                  })


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)

    return render(request,
                  'listings/band_detail.html',
                  {
                      'band_id': band_id,
                      'band': band,
                  })

def band_create(request):
    band_form = None

    if request.method == 'POST':

        band_form = BandForm(request.POST)

        if band_form.is_valid():
            # create an instance of Band
            band = band_form.save()

            return redirect('band-detail', band.id)

        else:
            pass
    else:
        band_form = BandForm()

    return render(request,
                  'listings/band_create.html',
                  {'band_form': band_form})


def about(request):
    return render(request,
                  'listings/about.html', )


def listing_list(request):
    listings = Listing.objects.all()

    return render(request,
                  'listings/listing_list.html',
                  {'listings': listings}, )

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)

    return render(request,
                  'listings/listing_detail.html',
                  {
                      'listing_id': listing_id,
                      'listing': listing,
                  })

def listing_create(request):
    listing_form = None

    if request.method == 'POST':

        listing_form = ListingForm(request.POST)

        if listing_form.is_valid():
            # create an instance of Band
            listing = listing_form.save()

            return redirect('listing-detail', listing.id)

        else:
            pass
    else:
        listing_form = ListingForm()

    return render(request,
                  'listings/listing_create.html',
                  {'listing_form': listing_form})

def contact(request):

    # logging
    print ("Request Method : ", request.method)
    print("Request Post Datas: ", request.POST)

    form = None # formulaire

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name'] or 'anonyme'} via Merchex Contact Form",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )

            return redirect('email-sent')
    else:
        form = ContactUsForm()

    return render(request,
                  'listings/contact.html',
                  {'form': form})

def email_sent(request):
    return render(request,
                  'listings/email_sent.html')
