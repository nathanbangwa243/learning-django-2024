from Tools.scripts.var_access_benchmark import read_dict
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View

from . import forms
from . import models


class PhotoUploadView(View, LoginRequiredMixin):
    template_name = 'blog/photo_upload.html'
    form_class = forms.PhotoForm

    def get(self, request):
        form = self.form_class()

        return render(request,
                      self.template_name,
                      context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)

            photo.uploader = request.user

            photo.save()

            return redirect('home')

        return render(request,
                      self.template_name,
                      context={'form': form})


@login_required
def home(request):
    photos = models.Photo.objects.all()

    return render(
        request,
        'blog/home.html',
        context={'photos': photos}
    )
