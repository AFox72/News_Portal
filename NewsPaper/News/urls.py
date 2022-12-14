from django.urls import path, include
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60 * 10)(PostList.as_view()), name='post_list'),
    path('<int:pk>', cache_page(300 * 10)(PostDetail.as_view()), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_edit'),
    path('<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
    ]