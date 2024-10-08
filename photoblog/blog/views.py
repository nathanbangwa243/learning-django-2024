from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.forms import formset_factory

from django.views.generic import View

from . import forms
from . import models


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


class EditBlogView(View, LoginRequiredMixin):
    template_name = "blog/edit_blog.html"
    edit_form_class = forms.BlogForm
    delete_form_class = forms.DeleteBlogForm

    def get(self, request, blog_id):
        blog = get_object_or_404(models.Blog, id=blog_id)

        edit_blog_form = self.edit_form_class(instance=blog)
        delete_blog_form = forms.DeleteBlogForm()

        context = {
            'edit_blog_form': edit_blog_form,
            'delete_blog_form': delete_blog_form,
        }

        return render(request,
                      self.template_name,
                      context=context)

    def post(self, request, blog_id):
        blog = get_object_or_404(models.Blog, id=blog_id)

        if 'edit_blog' in request.POST:
            edit_blog_form = self.edit_form_class(request.POST, instance=blog)

            if edit_blog_form.is_valid():
                edit_blog_form.save()
                return redirect('view_blog', blog_id=blog_id)
            else:
                pass
        else:
            pass

        if 'delete_blog' in request.POST:
            delete_blog_form = self.delete_form_class(request.POST)

            if delete_blog_form.is_valid():
                blog.delete()

                return redirect('home')
            else:
                pass

        else:
            pass

        context = {
            'edit_blog_form': edit_blog_form,
            'delete_blog_form': delete_blog_form,
        }

        return render(request,
                      self.template_name,
                      context=context)


class CreateMultiplePhotos(View, LoginRequiredMixin):
    template_name = 'blog/create_multiple_photos.html'
    PhotoFormSet = formset_factory(forms.PhotoForm, extra=3)

    def get(self, request):
        formset = self.PhotoFormSet()

        return render(request,
                      self.template_name,
                      context={'formset': formset})

    def post(self, request):
        formset = self.PhotoFormSet(request.POST, request.FILES)

        if formset.is_valid():
            print('FORMSET IS VALID')
            for form in formset:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.uploader = request.user
                    photo.save()
                else:
                    pass

            return redirect('home')
        else:
            print('FORMSET IS NOT VALID')

            pass

        return render(request,
                      self.template_name,
                      context={'formset': formset})


# FUNCTIONS BASE-VIEWS

@login_required
def home(request):
    photos = models.Photo.objects.all()

    return render(
        request,
        'blog/home.html',
        context={'photos': photos}
    )
