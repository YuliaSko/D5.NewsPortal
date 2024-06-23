from django.urls import path
from .views import (
   PostsList, ItemDetail, PostSearch, PostCreate, PostUpdate, PostDelete
)


urlpatterns = [
   path('', PostsList.as_view(), name='posts_list'),
   path('<int:pk>', ItemDetail.as_view(), name='item_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('create/', PostCreate.as_view(), name='news_create'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
