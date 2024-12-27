from django.urls import path
from movies import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addmovies, name='add'),
    path('search/', views.search, name= 'search'),
    path('<int:pk>/', views.detailPage, name= 'detail'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout')
]
