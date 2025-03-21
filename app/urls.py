from django.urls import path
from app import views
urlpatterns = [
    path('', views.home, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='signin'),
    path('settings/', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('search', views.search, name='serach'),
    path('like-post', views.liked_post, name='like-post'),
    path('follow', views.follow, name='follow'),
    path('logout/', views.logout, name='logout'),

]