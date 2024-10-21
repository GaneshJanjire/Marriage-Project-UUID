# from django.urls import path
# from .views import create_contact_info, contact_info

# urlpatterns = [
#     path('create/<uuid:uuid>/', create_contact_info, name='create_contact_info'),
#     path('info/<uuid:uuid>/', contact_info, name='contact_info'),
# ]


from django.urls import path
from .views import contact_info

urlpatterns = [
    path('ContactUs/<uuid:uuid>/', contact_info, name='contact_info'),  # Single endpoint for all methods
]
