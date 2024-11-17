from django.contrib import admin
from django.urls import path
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('recipes/' , recipes , name="recipes"),
    path('delete-recipe/<id>/' , delete_recipe , name="delete_recipe"),
    path('update-recipe/<id>/' , update_recipe , name="update_recipe"),
    path('login/' , login_page , name="login_page"),
    path('register/' , register, name="register"),
    path('logout/' , logout_page, name="logout_page"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()