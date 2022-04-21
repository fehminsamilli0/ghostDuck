from django.urls import path
from . import views

urlpatterns = [
    path('hello',views.say_hello),
    path('encription',functions.file_encrypter),
    path('decription',functions.file_decrypter)
]