from django.urls import path
from .views import *

urlpatterns = [
    path('' , home , name="home"),
    path("<int:pk>/"  , quiz_view),
    path("<int:pk>/data" , quiz_data_view),
    path("<int:pk>/save" , quiz_save_data)
]