from django.shortcuts import render
from .models import Persons

# Create your views here.
def home(request):
    return render(request, 'index.html')

def display(request):
    return render(request, 'display.html')

def login(request):
    if request.method == 'POST':
        in_email = request.POST.get('Email')
        in_passwd = request.POST.get('Passwd')
        try:
            data = Persons.objects.get(email=in_email)
            if in_passwd == data.password:
                context = {
                    'data': data,
                }
                return render(request, 'display.html', context)
            else:
                return render(request, 'login.html', {'message':'Incorrect Password!'})
        except:
            return render(request, 'login.html', {'message':'No Data Found!'})
        
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        in_name = request.POST.get('Name')
        in_age = request.POST.get('Age')
        in_gender = request.POST.get('Gender')
        in_email = request.POST.get('Email')
        in_passwd = request.POST.get('Passwd')

        data = Persons(name=in_name, age=in_age, gender=in_gender, email=in_email, password=in_passwd)
        data.save()
        return render(request, 'index.html', {'message':'User Registered Successfully!'})
    return render(request, 'signup.html')


