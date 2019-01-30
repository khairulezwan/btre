from django.urls import path #
from . import views #

#add url patterns
urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
]