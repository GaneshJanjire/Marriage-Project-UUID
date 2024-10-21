from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EducationDetails
from .serializers import EducationDetailsSerializer
from UserProfile_app.models import UserProfile

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def education_details(request, uuid):
    try:
        user = UserProfile.objects.get(uuid=uuid)
    except UserProfile.DoesNotExist:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    # Handle POST request to create education details
    if request.method == 'POST':
        serializer = EducationDetailsSerializer(data=request.data)
        if serializer.is_valid():
            education_info = serializer.save(user=user)
            return Response(
                {
                    "message": f"{user.name} {user.surname} Educational Details information",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle GET request to retrieve education details
    try:
        education_info = EducationDetails.objects.get(user=user)
    except EducationDetails.DoesNotExist:
        return Response({"message": "Educational details not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(
            {
                "message": f"{user.name} {user.surname} Educational Details information",
                "data": EducationDetailsSerializer(education_info).data
            },
            status=status.HTTP_200_OK
        )

    # Handle PUT or PATCH request to update education details
    elif request.method in ['PUT', 'PATCH']:
        serializer = EducationDetailsSerializer(education_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": f"{user.name} {user.surname} Education Details updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request to remove education details
    elif request.method == 'DELETE':
        education_info.delete()
        return Response(
            {"message": f"{user.name} {user.surname} Educational Details deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
