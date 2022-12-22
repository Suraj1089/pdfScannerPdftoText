from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )

def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successful")
            return redirect("index")
        else:
            messages.error(request,"Invalid credentials")
            return render(
                request,
                "login.html"
            )
    return render(
        request,
        "login.html",
    )


def signupUser(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST['email']
        password = request.POST["password"]
        confirm_password = request.POST['password2']
        # print(username,email,password,confirm_password)

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print("user name exit")
                messages.error(request,"Username already exists")
                return render(
                    request,
                    "signup.html"
                )
            elif User.objects.filter(email=email).exists():

                messages.error(request,"Email already exists")
                return render(
                    request,
                    "signup.html"
                )
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,"Account created successfully")
                return redirect("login")
        else:
            messages.error(request,"Password does not match")
            return render(
                request,
                "signup.html"
            )
    

    # print("hello nothing is doen")
    return render(
            request,
            "signup.html"
    )

   
def logoutUser(request):
    logout(request)
    messages.success(request,"Logout successful")
    return redirect("index")


def uploadPdf(request):
    if request.method == "POST":
        form = PdfForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PdfForm()
    return render(
        request,
        "upload.html",
        {
            "form":form
        }
    )