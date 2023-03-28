from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index),
    path('', views.PostList.as_view()),
    #path('<int:post_num>/', views.single_post_page)
    path('<int:pk>/', views.PostDetail.as_view()),
]