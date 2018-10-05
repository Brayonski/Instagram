from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NewsLetterForm

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def instagram(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = NewsLetterForm()
    return render(request, 'all-snaps/instagram.html', {"letterForm":form})
