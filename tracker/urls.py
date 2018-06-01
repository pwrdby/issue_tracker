from django.urls import path

from . import views

app_name = 'tracker'
urlpatterns = [
    path('<str:category>', views.IssueView.as_view(), name='index'),
    path('change_category/', views.change_category, name='change_cat'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:category_id>/update/', views.update, name='update')
]