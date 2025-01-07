from rest_framework import serializers
from .models import Book
from author.serializers import AuthorSerializer
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication



class BookSerializer(serializers.ModelSerializer):
    author_id=serializers.IntegerField(write_only=True)
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # author=AuthorSerializer(read_only=True)
    
    
    class Meta:
        model=Book
        fields=['id','title','rating','author_id']
        read_only_fields=['id']