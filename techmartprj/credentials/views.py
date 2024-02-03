from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.
def register(request):
    form=ProfileForm()
    return render(request,"register.html",{"form":form})