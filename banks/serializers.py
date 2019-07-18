from rest_framework import serializers

from .models import Banks, Branches


class BankSerializer(serializers.ModelSerializer):
    """
    Serializer for Banks
    """

    class Meta:
        model = Banks
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    """
    Serializer for Branches
    """
    bank = BankSerializer()

    class Meta:
        model = Branches
        fields = '__all__'
