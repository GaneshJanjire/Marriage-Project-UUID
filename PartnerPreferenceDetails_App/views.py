from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PartnerPreferenceDetails
from .serializers import PartnerPreferenceDetailsSerializer
from UserProfile_app.models import UserProfile

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def partner_preference_details(request, uuid):
    try:
        user = UserProfile.objects.get(uuid=uuid)
    except UserProfile.DoesNotExist:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = PartnerPreferenceDetailsSerializer(data=request.data)
        if serializer.is_valid():
            preference_info = serializer.save(user=user)
            return Response(
                {
                    "message": f"{user.name} {user.surname} Partner Preference Details information",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        preference_info = PartnerPreferenceDetails.objects.get(user=user)
    except PartnerPreferenceDetails.DoesNotExist:
        return Response({"message": "Partner preference details not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(
            {
                "message": f"{user.name} {user.surname} Partner Preference Details information",
                "data": PartnerPreferenceDetailsSerializer(preference_info).data
            },
            status=status.HTTP_200_OK
        )

    elif request.method in ['PUT', 'PATCH']:
        serializer = PartnerPreferenceDetailsSerializer(preference_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": f"{user.name} {user.surname} Partner Preference Details updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        preference_info.delete()
        return Response(
            {"message": f"{user.name} {user.surname} Partner Preference Details deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
