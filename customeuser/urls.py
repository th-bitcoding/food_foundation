from django.urls import path,include
from customeuser import views
urlpatterns = [
    
    path('',views.index,name='index')
]