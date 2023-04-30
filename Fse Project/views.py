from django.shortcuts import render, HttpResponse
from home.models import contact
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout

def index(request):
    return render(request,'index.html') 

def contact(request):
    if request.method=='POST':
        #jo name udhar wahi idhar aega
        name=request.POST['name']
        email=request.POST['email']
        content=request.POST['content']
        Contact=contact(fullname=name,email=email,content=content)
        Contact.save()
    return render(request, 'index.html')


def about(request):
    return HttpResponse('aboutus.html')
 
def search(request):
    query = request.GET['query']
    allposts = name.objects.filter(title__icontains=query)
    params= {'allpost':allpost}
    return render(request,'search.html')

def login_signup(request):
    return render(request, 'login_signup.html')


def handleSignup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        name=request.POST['name']
        pass1=request.POST['pass1']
       # pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('login_signup.html')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('login_signup.html')
        #if (pass1!= pass2):
         #    messages.error(request, " Passwords do not match")
          #   return redirect('login_signup.html')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= name
        myuser.save()
       
        return redirect('........home')

    else:
        return HttpResponse("404 - Not found")
    
def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

#def handelLogout(request):
   # logout(request)
   # messages.success(request, "Successfully logged out")
  #  return redirect('home')

def upload_file(request):
    if request.method == 'POST':
        form = UploadcodeForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle file upload
            title = form.cleaned_data['title']
            file = form.cleaned_data['file']
            # Do something with the uploaded file and title
            return redirect('upload_success')
    else:
        form = UploadcodeForm()
    return render(request, 'upload_file.html', {'form': form})
