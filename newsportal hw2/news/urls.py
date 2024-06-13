from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, ItemDetail


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', ItemDetail.as_view()),
]

