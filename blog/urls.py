from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name="post_new"),
    path('post/<int:pk>/update', views.post_update, name="post_update"),
    path('post/drafts', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/drafts', views.post_draft_publish, name="post_publish"),
    path('post/<int:pk>/remove', views.post_remove, name="post_remove"),
    path('post/<int:pk>/comment', views.add_comment_to_post, name="add_comment_to_post"),
    path('comment/<int:pk>/approve', views.comment_approve, name="comment_approve"),
    path('comment/<int:pk>/remove', views.comment_remove, name="comment_remove"),
]