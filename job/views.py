from django.shortcuts import render
from .models import Job # grab the model created in models and put it in dictionary then display it in web

# Create your views here.
def home(request):
    jobs = Job.objects.all
    return render(request, 'job/home.html', {'jobs': jobs})
