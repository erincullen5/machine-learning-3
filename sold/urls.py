from django.conf.urls import url
from sold import views

urlpatterns = [
  url(r'^data/$', views.sold_list),
  url('sold/', views.index)
]