from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View

from . import forms


class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''

        return render(
            request,
            self.template_name,
            context={
                'form': form,
                'message': message,
            }
        )

    def post(self, request):
        form = forms.LoginForm(request.POST)
        message = ''

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)

                return redirect('home')
            else:
                message = f"Login Failed"
        else:
            pass

        return render(
            request,
            self.template_name,
            context={
                'form': form,
                'message': message,
            }
        )


class LogoutUserView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect('login')


class SignUpView(View):
    template_name = "authentication/signup.html"
    form_class = forms.SignUpForm

    def get(self, request):
        form = self.form_class()

        return render(request,
                      self.template_name,
                      context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()

            # auto-login user
            login(request, user)

            return redirect(settings.LOGIN_REDIRECT_URL)

        else:
            return render(request,
                          self.template_name,
                          context={'form': form})


class UploadProfilePhoto(View, LoginRequiredMixin):
    template_name = "authentication/upload_profile_photo.html"
    form_class = forms.UploadProfilePhotoForm

    def get(self, request):
        form = self.form_class(instance=request.user)

        return render(request,
                      self.template_name,
                      context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('home')

        return render(request,
                      self.template_name,
                      context={'form': form})


# FUNCTIONS BASE-VIEWS

def logout_user(request):
    logout(request)
    return redirect('login')


def login_page(request):
    form = forms.LoginForm()
    message = ''

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)

                return redirect('home')
            else:
                message = f"Login Failed"
        else:
            pass
    else:
        form = forms.LoginForm()
        message = ''

    return render(
        request,
        'authentication/login.html',
        context={
            'form': form,
            'message': message,
        }
    )
