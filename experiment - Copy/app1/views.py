from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from app1.forms import RoomForm
from app1.models import Room, Uploads


def home(request):
    return render(request, 'app1/home.html')
# yo chai ho
def index(request):
    return render(request, 'index.html')


def send_files(request):
    if request.method == "POST":
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfoles")

        for f in myfile:
            print("yo print vaxa ki nai herum hai")
            print(room(request))
            Uploads(myfiles=f).save()

        return redirect("index")


def check(request):
    return render(request, 'app1/check.html')

def logoutUser(request):
    logout(request)
    return redirect('home')



def lr(request):
    page = 'login'
    print(page)
    if request.user.is_authenticated:
        redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        try:
            user = User.objects.get(username=username)
            print("try ko user print vako hai guys")
            print(user)
        except:
            messages.error(request, 'Document deleted.')


        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print("lau yo po chalya")
            print(user)
            return redirect('room')
        else:
            messages.error(request,'userdoes not exixts')

    context={'page':page}
    return render(request, 'app1/check.html',context)

def room(request):
    roomed = Room.objects.all()
    print(roomed)
    print('his is the descrpition buddy')

    context = {'room': roomed}
    return render(request, 'app1/check.html',context)

def form(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'app1/Fomr.html',context)

def add(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            messages.success(request, 'Posted in room.')
            return redirect('home')
        print(request.POST)
    print(room)
    context = {'form': form}
    return render(request, 'app1/Fomr.html', context)

