from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserForm, ContactForm
from .models import User, Contact

owner_name = ''


# Create your views here.

def index(request):
    if request.method == 'POST':
        btn_pressed = request.POST.get('btn')
        if btn_pressed == 'login':
            return redirect('log_in')
        if btn_pressed == 'sing_on':
            return redirect('sing_on')
    else:
        return render(request, 'user/index.html')


def sing_on(request):
    global owner_name
    if request.method == 'POST':
        try:
            form_user = UserForm(request.POST)
            if form_user.is_valid():
                owner_name = request.POST.get("username")
                form_user.save()
                return redirect('add_contact')
        except:
            message = "something went wrong"
            return render(request, 'user/sing_on.html', {'message': message})

    else:
        form_user = UserForm()
        return render(request, 'user/sing_on.html', {'form': form_user})


def log_in(request):
    if request.method == 'POST':
        try:
            username_or_email = request.POST.get('username')
            password = request.POST.get('password')
            if '@' in username_or_email:
                form = User.objects.get(email=username_or_email)
            else:
                form = User.objects.get(username=username_or_email)
            if form.password == password:
                form = Contact.objects.filter(owner=form.id)
                return render(request, 'user/show_contact.html', {'form': form})
        except:
            message = f"Something went wrong your username or password is incorrect."
            return render(request, 'user/login.html', {'message': message})
    else:
        return render(request, 'user/login.html', )


def add_contact(request):
    global owner_name
    if request.method == 'POST':
        try:
            if request.POST.get('btn') == 'submit_contact':
                contact = request.POST.get('contact')
                owner_name = User.objects.get(username=owner_name)
                phone_number = request.POST.get('phone_number')
                Contact.objects.create(owner=owner_name, contact=contact, phone_number=phone_number)
        except:
            message = f"Something went wrong choose another name."
            return render(request, 'user/add_contact.html', {'message': message})

    form = ContactForm()
    return render(request, 'user/add_contact.html', {'form': form})


def show_contact(request):
    global owner_name
    try:
        form = Contact.objects.filter(owner=owner_name)
        return render(request, 'user/show_contact.html', {'form': form})
    except:
        message = "Something went wrong maby you didnt add contact"
        return redirect('add_contact', {'message': message})


