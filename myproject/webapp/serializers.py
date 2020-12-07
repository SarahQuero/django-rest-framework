from rest_framework import serializers
from . models import employees

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = ('firstname', 'lastname', 'user_email', 'postal_address', 'active')
        # fields = '__all__'