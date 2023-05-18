from rest_framework import serializers

from .models import AddressBook


class AddressBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressBook
        fields = "__all__"


