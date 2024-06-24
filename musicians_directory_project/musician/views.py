from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_musician(request):
    if request.method =='POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form' : musician_form})


def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=musician)

    if request.method =='POST': # user sent POST request
        musician_form = forms.MusicianForm(request.POST, instance=musician)  # capture the user post data
        if musician_form.is_valid(): # checking the post data validation
            musician_form.save() # if data valid save in the database
            return redirect('homepage')  # redirect to the page 
    return render(request, 'add_musician.html', {'form' : musician_form})