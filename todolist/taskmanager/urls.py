from django.urls import path
from .views import home, add_task, edit_task, delete_task, task_details, search_view, dashboard
urlpatterns = [
    
    path('dashboard/', dashboard, name='dashboard'),
    path('', home, name='home'),
    path('addtask/', add_task, name='add_task'),
    path('<int:pk>/edit/', edit_task, name='edit_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('details<int:pk>/', task_details, name='task_body'),
    path('search/', search_view, name='search'),
]
