from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": f"{user.name} {user.surname} registered successfully",
                    "uuid": str(user.uuid),
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    try:
        user = UserProfile.objects.get(username=request.data['username'])
        if user.password == request.data['password']:
            return Response(
                {
                    "message": f"{user.username} logged in successfully",
                    "uuid": str(user.uuid),
                    "data": UserProfileSerializer(user).data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "You entered wrong password, please rewrite the correct password."},
                status=status.HTTP_400_BAD_REQUEST
            )
    except UserProfile.DoesNotExist:
        return Response(
            {"message": f"{request.data['username']} is not registered."},
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def user_profile(request, uuid, username):
    try:
        user = UserProfile.objects.get(uuid=uuid, username=username)
    except UserProfile.DoesNotExist:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(
            {
                "message": f"{user.name} {user.surname} all information",
                "data": UserProfileSerializer(user).data
            },
            status=status.HTTP_200_OK
        )
    # Other methods (PUT, PATCH, DELETE) go here

# def user_profile(request, uuid, username):
#     try:
#         user = UserProfile.objects.get(uuid=uuid, username=username)
#     except UserProfile.DoesNotExist:
#         return Response({"message": f"User not found."}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         return Response(
#             {
#                 "message": f"{user.name} {user.surname} all information",
#                 "data": UserProfileSerializer(user).data
#             },
#             status=status.HTTP_200_OK
#         )

    elif request.method in ['PUT', 'PATCH']:
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
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

    elif request.method == 'DELETE':
        user.delete()
        return Response(
            {"message": f"{user.name} {user.surname} data deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
