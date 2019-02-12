from django.urls import path  # IMPORT THIS
from . import views  # IMPORT THIS

# add url patterns

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]