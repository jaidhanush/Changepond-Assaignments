from rest_framework import serializers
from .models import dish
from Chief.serializers import ChiefSerializer



class DishSerializer(serializers.ModelSerializer):
    Chief_id=serializers.IntegerField(write_only=True)
    # author=AuthorSerializer(read_only=True)
    
    
    class Meta:
        model=dish
        fields=['dishname','rating',"Chief_id"]
        read_only_fields=['id']