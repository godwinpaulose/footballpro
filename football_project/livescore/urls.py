
from django.urls import path
from . import views
app_name='livescore'

urlpatterns = [

    path('',views.new,name='new'),
    path('team/<int:id>/',views.details,name='details'),
    path('add/',views.add_team,name='add_team'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),


]