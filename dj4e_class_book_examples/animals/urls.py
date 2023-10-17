from django.urls import path
from animals import views
from django.views.generic.base import TemplateView


app_name = 'animals'
urlpatterns = [
    path('', views.CatListView.as_view(), name='cat_list'),
    path('<int:pk>/', views.CatDetailView.as_view(), name='cat_details'),
    path('new/', views.CatNewView.as_view(), name='cat_new'),
    path('create/',TemplateView.as_view(template_name = 'cat_new.html'), name='create'),

]