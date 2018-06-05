from django.urls import path

from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.IssueView.as_view()),
    path('<str:category>', views.IssueView.as_view(), name='index'),
    path('change_category/', views.change_category, name='change_cat'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]