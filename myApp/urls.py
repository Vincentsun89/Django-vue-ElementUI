from django.conf.urls import url

from myApp import views

urlpatterns = [
    url('add_student/',views.add_student),
    url('show_students/',views.show_students),
    
]
