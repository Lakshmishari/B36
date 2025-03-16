from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'home' with your desired home page URL
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None

    return render(request, 'accounts/login.html', {'error_message': error_message})


#def home(request):
#    return render(request,'accounts/home.html', {'userName' : request.user.username})



from .forms import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with the name of your login URL pattern
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})

def logout_user(request):
    logout(request)
    #return redirect('login')
    return redirect('index')