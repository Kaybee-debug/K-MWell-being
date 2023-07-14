from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User,auth
# from django.contrib import messages

def register(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()  # <-- this will create a new listing
            user = form.cleaned_data.get('username')
            messages.success(request,'account created for'+ user)
            return redirect("/")
    
    context = {
        'form': form
    }
    return render(request,'register.html',context)
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']
    
#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request,'Email Already Exists')
#                 return redirect('register')
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request,'Username Already Exists')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username,email=email,password=password)
#                 user.save();
#                 print('user created')
#                 return redirect('login')
#         else:
#             messages.info(request,'Password Not The Same')
#             return redirect('register')
#     else:
#         return render(request,'register.html')

def logins(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html') 
# def logoutUser(request):
#     logout(request)
#     return redirect("login")