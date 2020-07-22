from django.shortcuts import render, redirect
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']

    errors = User.objects.register_validate(request.POST)
    if len(errors) > 0:
        # CREATE THE ERROR MESSAGES
        return redirect("/")
    # CREATING A USER
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print(pw_hash)
    user = User.objects.create(first_name=first_name, last_name=last_name, email=email ,password=pw_hash)
    request.session['user_id'] = user.id
    return redirect("/homepage")

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect("/homepage")
    return redirect("/")