from django.urls import path #IMPORT THIS
from . import views #IMPORT THIS

#add url patterns
urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
]