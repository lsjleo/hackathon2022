from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
# from django.views.generic import TemplateView

urlpatterns = [
    path('home/', index, name = "home"),
    path('ia/', ia, name = "ia")
] + staticfiles_urlpatterns()