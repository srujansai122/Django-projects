from django.urls import path
from . import views

app_name="food"

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:id>/',views.detail,name="detail"),
    path('create/', views.create_item,name="Itemform"),
    path('edit/<int:id>/',views.edit_item,name="editItem"),
    path('delete/<int:id>/',views.delete_item,name="deleteItem"),
]
