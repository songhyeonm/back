from django.urls import path

import views

urlpatterns = [
    path('read', views.read),

]