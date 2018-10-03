from django.conf.urls import url
from jack import views

urlpatterns = [
  url('jack/', views.index)
]