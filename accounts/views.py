from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contacts.models import Contact
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # Get for values

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match

        if password == password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username taken')
                return redirect('register')
            else:
                # Check Email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already been used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
                    # Login after register
        else:
            messages.error(request, 'Passwords do no match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

@login_required(login_url='login')
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)