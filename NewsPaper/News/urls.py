from django.urls import path, include
from .views import (
    PostList, PostDetail, PostCreate, PostUpdate, PostDelete
)

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/create/', PostCreate.as_view(), name='post_edit'),
    path('articles/create/', PostCreate.as_view(), name='post_edit'),
    path('<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

]