from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserForm, ContactForm
from .models import User, Contact


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
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            print("1111111111111111111111111111")
            user = request.POST.get('username')
            print(user)
            form_user.save()
            return redirect('add_contact')

    else:
        form_user = UserForm()
        return render(request, 'user/sing_on.html', {'form': form_user})


def log_in(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        if '@' in username_or_email:
            form = User.objects.get(email=username_or_email)
        else:
            form = User.objects.get(username=username_or_email)
        if form.password == password:
            form = Contact.objects.filter(owner=form.id)
            return render(request, 'user/show_contact.html', {'form':form})
    else:
        return render(request, 'user/login.html', )


def add_contact(request):
    if request.method == 'POST':
        btn_pressed = request.POST.get('btn')
        if btn_pressed == 'submit':
            form = Contact(request.POST)
            if form.is_valid():
                form.save()
        if btn_pressed == 'show_contact':
            pass
    form = ContactForm()
    return render(request, 'user/add_contact.html', {'form': form})