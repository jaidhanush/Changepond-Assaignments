from rest_framework import serializers
from .models import chief


class ChiefSerializer(serializers.ModelSerializer):
    class Meta:
        model = chief
        fields="__all__"  #[id,name,age]
        read_only_field=['id']