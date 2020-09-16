from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.apiOverview, name="ApiOverview"),
    path('api/task-list/', views.taskList, name="Task-List"),
    path('api/task-detail/<str:pk>/', views.taskDetail, name="Task-Detail"),
    path('api/task-create/', views.taskCreate, name="Task-Create"),
    path('api/task-update/<str:pk>/', views.taskUpdate, name="Task-Update"),
    path('api/task-delete/<str:pk>/', views.taskDelete, name="Task-Delete"),
]
