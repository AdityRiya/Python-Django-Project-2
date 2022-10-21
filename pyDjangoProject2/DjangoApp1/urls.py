from django.conf.urls import url 
from DjangoApp1 import views
urlpatterns = [
    path("",views.users,name='users'),
    
]
