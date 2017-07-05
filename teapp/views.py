from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from teapp.models import Event_Details,Categories
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


#from __future__ import unicode_literals
# Create your views here.
def images(request):
    return render(request,'teapp/images.html',{})

def Home_page(request):
    return render(request,'teapp/Home_page.html',{})

def Internship(request):
    #e_list = Event_Details.objects.all
    e_list =  Event_Details.objects.filter(category='internship')
# city_list=Event_Details.objects.all
    rendered=render(request,'teapp/internship_choices.html',context={'Internship_Events':e_list})
    return HttpResponse(rendered)

def Interndetails(request):
    my_filter={
            'category':"internship",
            'city':"Hyderabad",
            }
    e_list_bychoice=Event_Details.objects.filter(**my_filter)
    rendered= render(request,'teapp/event_details.html',context={'Internship_details_byplace':e_list_bychoice})
    return HttpResponse(rendered)
     #  return HttpResponseRedirect("/teapp/event_details.html/")
     
     
     
     
     
     

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'teapp/signup.html', {'form': form})
     
     
     
