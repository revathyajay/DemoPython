from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [

    path('', views.add, name='add'),
    path('delete1/<int:taskid>/', views.delete1, name='delete1'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.Tasklistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.Taskdetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete'),
]
