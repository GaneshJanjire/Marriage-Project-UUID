from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HoroscopeDetails
from .serializers import HoroscopeDetailsSerializer
from UserProfile_app.models import UserProfile

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def horoscope_details(request, uuid):
    try:
        user = UserProfile.objects.get(uuid=uuid)
    except UserProfile.DoesNotExist:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    # Handle POST request to create horoscope details
    if request.method == 'POST':
        serializer = HoroscopeDetailsSerializer(data=request.data)
        if serializer.is_valid():
            horoscope_info = serializer.save(user=user)
            return Response(
                {
                    "message": f"{user.name} {user.surname} Horoscope information",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle GET request to retrieve horoscope details
    try:
        horoscope_info = HoroscopeDetails.objects.get(user=user)
    except HoroscopeDetails.DoesNotExist:
        return Response({"message": "Horoscope information not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(
            {
                "message": f"{user.name} {user.surname} Horoscope information",
                "data": HoroscopeDetailsSerializer(horoscope_info).data
            },
            status=status.HTTP_200_OK
        )

    # Handle PUT or PATCH request to update horoscope details
    elif request.method in ['PUT', 'PATCH']:
        serializer = HoroscopeDetailsSerializer(horoscope_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": f"{user.name} {user.surname} Horoscope Details updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request to remove horoscope details
    elif request.method == 'DELETE':
        horoscope_info.delete()
        return Response(
            {"message": f"{user.name} {user.surname} Horoscope Details deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
