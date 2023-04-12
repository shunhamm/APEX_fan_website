from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('rules/', views.rules(), name="rules"),
    # path('notables/int:notablesIndex/', views.notables_detail(), name="notables_detail"),
    # path('notables/', views.notables_list(), name="notables_list"),
    # path('externalLinks/', views.external_links(), name="external_links")
]
