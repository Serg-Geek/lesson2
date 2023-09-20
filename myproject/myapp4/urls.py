from django.urls import path
from .views import user_form
from .views import many_field_form
from .views import add_user
from .views import upload_image



urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms/', many_field_form, name='many_field_form'),
    path('user/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),
]
