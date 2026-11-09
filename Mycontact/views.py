from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .forms import  contactform2, contactform3

def controleform1(request):
    if request.method == "POST":
        f = request.POST['firstname']
        l = request.POST['lastname']
        e = request.POST['email']
        m = request.POST['message']

        contact = Contact.objects.create(
            firstname=f,
            lastname=l,
            email=e,
            message=m
        )

        return HttpResponse('<h2>Data has been submitted</h2>')

    return render(request, "myform1.html")

# Create your views here.

def controleform2(request):
    form = contactform2(request.POST)

    if request.method == "POST":
        if form.is_valid():
            f = form.cleaned_data['name']
            l = form.cleaned_data['lastname']
            e = form.cleaned_data['email']
            m = form.cleaned_data['message']

            contact = Contact.objects.create(firstname=f, lastname=l, email=e, message=m)
            return HttpResponse('<h2>Data has been submitted</h2>')
        else:
            form = contactform2()
    return render(request, "myform2.html", {'form': form})

def controleform3(request):
    form = contactform3(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Data has been submitted</h2>')
    else:
        form = contactform3()
    return render(request, "myform3.html", {'form': form})


