from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login as Login , logout as Logout 
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            Login(request, form.save())
            return redirect("posts:list")
    else:
        form = UserCreationForm()

        
    return render(request , "users/register.html" , {'form' :form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
 
        if(form.is_valid()):
            user = form.get_user()
            Login(request , user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
            


    else:
        form = AuthenticationForm()
    return render(request , "users/login.html" , {'form' : form})

def logout(request):
    if request.method == 'POST':
        Logout(request)
    return redirect("posts:list")
    