from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.loginView, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutView, name="logout"),

    path('create-post', views.createView, name="create-post"),
    path('details-page/<int:pk>/', views.detailsView, name="details-page"),

    path('update-post/<int:pk>/', views.updateView, name="update-post"),
    # path('update-comment/<int:pk>/', views.updateView, name="update-comment"),

    path('delete-post/<int:pk>/', views.deleteView, name="delete-post"),
    path('delete-comment/<int:pk>/', views.deleteMessage, name="delete-comment"),
]
