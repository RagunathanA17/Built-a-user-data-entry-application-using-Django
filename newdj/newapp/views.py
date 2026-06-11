from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

def index(request):
    return render(request, "newapp/index.html")

def userinputview(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")

        Employee.objects.create(
            Firstname=fname,
            Lastname=lname,
            Email=email,
            Mobile=mobile,
        )

    return HttpResponse("Data Stored...")

# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.

# def index(request):
#     return render(request, "newapp/index.html")

# def userinputview(request):
#     firstname = request.POST['fname']
#     lastname = request.POST['lname']
#     email = request.POST['email']
#     mobile = request.POST['mobile']

#     newuser = Employee.objects.create(
#         Firstname = firstname,
#         Lastname = lastname,
#         Email = email,
#         Mobile = mobile,
#     )
    
#     return HttpResponse("Data Stored Successfully...")