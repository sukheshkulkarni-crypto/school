from django.urls import path
from . import views
urlpatterns=[
path('',views.staff_list),
path('create/',views.staff_create),
path('update/<int:id>/',views.staff_update),
path('delete/<int:id>/',views.staff_delete),
]