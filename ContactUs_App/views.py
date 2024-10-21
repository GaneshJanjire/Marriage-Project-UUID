# from django.shortcuts import render

# # Create your views here.
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import ContactUs
# from .serializers import ContactUsSerializer
# from UserProfile_app.models import UserProfile

# @api_view(['POST'])
# def create_contact_info(request, uuid):
#     try:
#         user = UserProfile.objects.get(uuid=uuid)
#     except UserProfile.DoesNotExist:
#         return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'POST':
#         serializer = ContactUsSerializer(data=request.data)
#         if serializer.is_valid():
#             contact_info = serializer.save(user=user)
#             return Response(
#                 {
#                     "message": f"{user.name} {user.surname} information",
#                     "data": serializer.data
#                 },
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def contact_info(request, uuid):
#     try:
#         user = UserProfile.objects.get(uuid=uuid)
#         contact_info = ContactUs.objects.get(user=user)
#     except (UserProfile.DoesNotExist, ContactUs.DoesNotExist):
#         return Response({"message": "Contact information not found."}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         return Response(
#             {
#                 "message": f"{user.name} {user.surname} information",
#                 "data": ContactUsSerializer(contact_info).data
#             },
#             status=status.HTTP_200_OK
#         )

#     elif request.method in ['PUT', 'PATCH']:
#         serializer = ContactUsSerializer(contact_info, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     "message": f"{user.name} {user.surname} data updated successfully",
#                     "data": serializer.data
#                 },
#                 status=status.HTTP_200_OK
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         contact_info.delete()
#         return Response(
#             {"message": f"{user.name} {user.surname} data deleted successfully"},
#             status=status.HTTP_204_NO_CONTENT
#         )



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactUs
from .serializers import ContactUsSerializer
from UserProfile_app.models import UserProfile

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def contact_info(request, uuid):
    try:
        user = UserProfile.objects.get(uuid=uuid)
    except UserProfile.DoesNotExist:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    # Handle POST request to create contact information
    if request.method == 'POST':
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            contact_info = serializer.save(user=user)
            return Response(
                {
                    "message": f"{user.name} {user.surname} information",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle GET request to retrieve contact information
    try:
        contact_info = ContactUs.objects.get(user=user)
    except ContactUs.DoesNotExist:
        return Response({"message": "Contact information not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(
            {
                "message": f"{user.name} {user.surname} information",
                "data": ContactUsSerializer(contact_info).data
            },
            status=status.HTTP_200_OK
        )

    # Handle PUT or PATCH request to update contact information
    elif request.method in ['PUT', 'PATCH']:
        serializer = ContactUsSerializer(contact_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": f"{user.name} {user.surname} data updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request to remove contact information
    elif request.method == 'DELETE':
        contact_info.delete()
        return Response(
            {"message": f"{user.name} {user.surname} data deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
