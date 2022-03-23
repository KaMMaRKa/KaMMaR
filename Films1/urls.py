from django.urls import path
from Films1 import views

urlpatterns = [
    path('404', views.getNotFound),
    path('<name>', views.getFilmscat),
    path('', views.getmainpage)
]
