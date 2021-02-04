from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name='homepage'),
    path('howto/', views.howto , name='howto'),
    path('history/', views.history , name='history'),
    path('QandH/', views.QandH , name='Q&H'),
    path('visa/', views.visa , name='visa'),
    path('agents/', views.agents , name='agents'),
    path('hotels/', views.hotels , name='hotels'),
    path('rental/', views.rentals , name='rentals'),
    path('flights/', views.flights , name='flights'),
    path('blog/', views.rentals , name='blog'),
]