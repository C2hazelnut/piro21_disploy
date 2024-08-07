from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
  path('', main, name='main'), #name을 사용하면, url을 변경시에 유지보수가 쉬움.
  path('create/', create, name='create'),
  path('detail/<int:pk>/', detail, name='detail'),
  path('delete/<int:pk>/', delete, name='delete'),
  path('update/<int:pk>/', update, name='update'),
]