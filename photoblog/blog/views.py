from django.shortcuts import render, redirect, get_object_or_404
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


class BlogAndPhotoUploadView(View, LoginRequiredMixin):
    template_name = 'blog/create_blog_post.html'

    blog_form_class = forms.BlogForm
    photo_form_class = forms.PhotoForm

    def get(self, request):
        blog_form = self.blog_form_class()
        photo_form = self.photo_form_class()

        context = {
            'blog_form': blog_form,
            'photo_form': photo_form,
        }

        return render(request,
                      self.template_name,
                      context=context)

    def post(self, request):
        blog_form = self.blog_form_class(request.POST)
        photo_form = self.photo_form_class(request.POST, request.FILES)

        if all([blog_form.is_valid(), photo_form.is_valid()]):
            # link photo to user, then save it
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()

            # link lo to photo and user, then save it
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()

            # redirect to home page
            return redirect('home')
        else:
            pass

        context = {
            'blog_form': blog_form,
            'photo_form': photo_form,
        }

        return render(request,
                      self.template_name,
                      context=context)


class ViewBlogView(View, LoginRequiredMixin):
    template_name = 'blog/view_blog.html'

    def get(self, request, blog_id):
        blog = get_object_or_404(models.Blog, id=blog_id)

        return render(request,
                      self.template_name,
                      context={'blog': blog})


class HomeView(View, LoginRequiredMixin):
    template_name = 'blog/home.html'

    def get(self, request):
        photos = models.Photo.objects.all()
        blogs = models.Blog.objects.all()

        return render(
            request,
            'blog/home.html',
            context={'photos': photos, 'blogs': blogs, }
        )


# FUNCTIONS BASE-VIEWS

@login_required
def home(request):
    photos = models.Photo.objects.all()

    return render(
        request,
        'blog/home.html',
        context={'photos': photos}
    )
