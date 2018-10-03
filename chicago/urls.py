from django.conf.urls import url
from chicago import views

urlpatterns = [
  url('', views.index)
]