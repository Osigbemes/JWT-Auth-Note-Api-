from http.client import FOUND, NOT_FOUND
from multiprocessing import AuthenticationError
from sre_constants import SUCCESS
from webbrowser import get
from django.http import JsonResponse
from pandas import notnull
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import NoteSerializer, UserSerializer, UserVmSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from base.models import Note, User

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]

    return Response(routes)

class RegisterUserView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=AuthenticationError):
            serializer.save()
        return Response(serializer.data)

class GetUserView(APIView):

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserVmSerializer(user)
        if serializer:
            return Response(serializer.data)
        return Response(serializer.errors)

class GetAllUserView(APIView):
    
    def get(self, request):
        user = User.objects.all()
        serializer = UserVmSerializer(user, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteUserView(APIView):
    
    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        if not user:
            return Response("User not found!")
            
        user.delete()
        return Response("User deleted successfully!")

class LoginView(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        #get the wtoke of the user
        token = super().get_token(user)

        #Add custom claims
        token['username']=user.username
        token['email']=user.email
        return token

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # here we are extending the serializer class by customizing the token.
    @classmethod
    def get_token(cls, user):
        #get the token of the user by overwriting the function in the class
        token = super().get_token(user)

        #Add custom claims
        token['username']=user.name
        #token['password']=user.password
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all() #returns the notes of this user
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postNotes(request):
    permission_classes = []
    note = NoteSerializer(data=request.data)
    if note.is_valid():
        note.save()
    return Response(note.data)
