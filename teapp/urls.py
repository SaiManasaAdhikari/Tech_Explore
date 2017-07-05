from django.conf.urls import url
from teapp import views
#from techexplore.teapp import views as teapp_views
from django.contrib import admin
urlpatterns=[
          url(r'^images/$',views.images,name='image'),
          url(r'^$', views.Home_page, name='home'),
          url(r'^intern$', views.Internship, name='internship'),
          url(r'^event_details.html$',views.Interndetails,name='event'),
          url(r'^signup/$', views.signup, name='signup'),
        ]
        
