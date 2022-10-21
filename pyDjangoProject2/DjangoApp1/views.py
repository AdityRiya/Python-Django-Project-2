from django.shortcuts import render
from DjangoApp1 import User
# Create  your views here.
def index(request):
    return render(request,'index.html')
def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user': user_list}
    return render(request,'users.html',context=user_dict)
