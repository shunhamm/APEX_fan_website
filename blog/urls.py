from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_character_detail, name="random_character_detail"),
    path('character_detail/<str:character_name>/', views.character_detail, name="character_detail"),
    # path('notables/', views.notables_list(), name="notables_list"),
    # path('externalLinks/', views.external_links(), name="external_links")
]
