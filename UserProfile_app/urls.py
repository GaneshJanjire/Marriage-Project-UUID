from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import register, login, user_profile

from django.urls import path
from .views import register, login, user_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/<uuid:uuid>/<str:username>/', user_profile, name='user_profile'),  # Ensure this line is correct
]



# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)