from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def instagram(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Brian Mutai']
            email = form.cleaned_data['kiprotichbrian8@gmail.com']
            recipient = NewsLetterForm(name = name, email = email)
            recipient.save()
            HttpResponseRedirect('instagram')
    else:
        form = NewsLetterForm()
    return render(request, 'all-snaps/instagram.html', {"letterForm":form})
