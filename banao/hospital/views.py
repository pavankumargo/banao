from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Users

# Create your views here.
def home(request):
    return render(request,"home.html")


def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        line=request.POST['line']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        user_type=request.POST['user_type']
        password=request.POST['password']
        password1=request.POST['password1']
        if password != password1:
            messages.info(request,'Passwords do not match')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
        if Users.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
        if len(request.FILES)!=0:
            myfile=request.FILES['pic']
            Users.objects.create(username=username,email=email,first_name=first_name,last_name=last_name,profile=myfile,line=line
            ,city=city,state=state,pincode=pincode,user_type=user_type)
        else:
            Users.objects.create(username=username,email=email,first_name=first_name,last_name=last_name,line=line
                ,city=city,state=state,pincode=pincode,user_type=user_type)
        user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name)
        user.save()
        return redirect('login')
    else:
        return render(request,'register.html')


def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['username']=username
            per=Users.objects.get(username=username)
            if per.user_type=='Doctor':
                return redirect('dlogin')
            else:
                return redirect('plogin')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def plogin(request):
    username=request.session['username']
    pat=Users.objects.get(username=username)
    context={
        'pat' :pat,
    }
    return render(request,'pdashboard.html',context)


def dlogin(request):
    username=request.session['username']
    doc=Users.objects.get(username=username)
    context={
        'doc' :doc,
    }
    return render(request,'ddashboard.html',context)


def logout(request):
    auth.logout(request)
    return redirect('/')
