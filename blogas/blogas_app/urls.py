from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path("post/<slug:pk>", views.PostDetailView.as_view(), name="post") # nurodyti pk, kad zinotu kuri objekta issikviesti
]
