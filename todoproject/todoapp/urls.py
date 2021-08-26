from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('index/',views.listview.as_view(),name='index'),
    path('detail/<int:pk>/',views.detailview.as_view(),name='detail'),
    path('update/<int:pk>/',views.updateview.as_view(),name='update'),
    path('delete/<int:pk>/',views.deleteview.as_view(),name='delete')
]

