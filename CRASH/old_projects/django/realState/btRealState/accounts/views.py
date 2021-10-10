from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from inquiries.models import Contact
# Create your views here.


def login(request):
    if request.method == 'POST':
        # Get Field Values
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate and Login
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have logged out of your account!')
        return redirect('index')

    else:
        return redirect('index')


def register(request):
    if request.method == 'POST':
        # Get Form Values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check if username exists
            if User.objects.all().filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                # Check if email exists
                if User.objects.all().filter(email=email).exists():
                    messages.error(request, 'Username already exists!')
                    return redirect('register')
                else:
                    # There You Go!
                    user = User.objects.create_user(
                        username=username, email=email, password=password)
                    user.save()
                    messages.success(
                        request, 'You are registered and can log in!')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    allcontacts = Contact.objects.all().order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': allcontacts
    }
    return render(request, 'accounts/dashboard.html', context)
