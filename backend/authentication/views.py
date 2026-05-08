from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib import messages

from .forms import LoginForm


def login_view(request):

    if request.user.is_authenticated:

        return redirect('/dashboard/')

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            username = form.cleaned_data.get(
                'username'
            )

            password = form.cleaned_data.get(
                'password'
            )

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect(
                    '/dashboard/'
                )

        messages.error(
            request,
            'Invalid Username or Password'
        )

    context = {
        'form': form
    }

    return render(
        request,
        'authentication/login.html',
        context
    )


def logout_view(request):

    logout(request)

    return redirect('/login/')