from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Habbits_Interest
from .serializers import HabbitsInterestSerializer
from UserProfile_app.models import UserProfile

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def habbits_interest_details(request, uuid):
    try:
        user = UserProfile.objects.get(uuid=uuid)
    except UserProfile.DoesNotExist:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = HabbitsInterestSerializer(data=request.data)
        if serializer.is_valid():
            interest_info = serializer.save(user=user)
            return Response(
                {
                    "message": f"{user.name} {user.surname} Hobbies and Interest Details information",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        interest_info = Habbits_Interest.objects.get(user=user)
    except Habbits_Interest.DoesNotExist:
        return Response({"message": "Hobbies and Interest details not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(
            {
                "message": f"{user.name} {user.surname} Hobbies and Interest Details information",
                "data": HabbitsInterestSerializer(interest_info).data
            },
            status=status.HTTP_200_OK
        )

    elif request.method in ['PUT', 'PATCH']:
        serializer = HabbitsInterestSerializer(interest_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": f"{user.name} {user.surname} Hobbies and Interest Details updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        interest_info.delete()
        return Response(
            {"message": f"{user.name} {user.surname} Hobbies and Interest Details deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
