from django.urls import path
from .views import (
   PostsList, ItemDetail, PostSearch, PostCreate, PostUpdate, PostDelete, CategoryPostList, subscribe
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
   path('category/<int:pk>', CategoryPostList.as_view(), name='category_list'),
   path('category/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('create/limit', PostCreate.as_view(), name='news_limit'),
   path('articles/create/limit', PostCreate.as_view(), name='articles_limit'),

]
