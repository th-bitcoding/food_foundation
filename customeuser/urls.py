from django.urls import path,include
from customeuser import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('product/',views.product,name='product'),
    path('contact/',views.contact,name='contact'),
    path('UserAdd/',views.UserApiView.as_view(),name='UserAdd'),



]