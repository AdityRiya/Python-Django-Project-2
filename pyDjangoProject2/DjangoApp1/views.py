from django.shortcuts import render
from DjangoApp1 import User
# Create  your views here.
def index(request):
    return render(request,'index.html')
def user(request):
    user_list = User.ob