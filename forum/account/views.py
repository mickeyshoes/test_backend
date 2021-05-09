from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from .models import User
from .serializers import CreateAndModifyUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    
    if request.method == 'POST':
        serializer = CreateAndModifyUserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'message' : 'input data isn\'t valid'}, status=status.HTTP_412_PRECONDITION_FAILED)

        if User.objects.filter(login_id=serializer.validated_data['login_id']).first() is not None:
            return Response({'message' : 'ID already exists'}, status=status.HTTP_412_PRECONDITION_FAILED)

        if User.objects.filter(email=serializer.validated_data['email']).first() is not None:
            return Response({'message' : 'email already exists'}, status=status.HTTP_412_PRECONDITION_FAILED)

        serializer.save()
        print(serializer.data)
        return Response({'message' : "success"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    if request.method == 'POST':
        try:
            user = User.objects.get(login_id=request.data['login_id'])
            if not user.check_password(request.data['password']):
                return Response({'message' : 'password does not match'}, status=status.HTTP_400_BAD_REQUEST)

            response = refresh_token(user)
            return Response(response, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'message' : 'input ID is not enrolled'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'message' : 'there is no matching data', 'login_id' : 'required', 'password' : 'required'}, status=status.HTTP_400_BAD_REQUEST)
 
def refresh_token(user) -> dict:
    refresh = RefreshToken.for_user(user)
    response = {
        'message' : 'success',
        'refresh' : str(refresh),
        'token' : str(refresh.access_token),
    }

    return response