import re
from rest_framework import serializers
from bandwidth.models import Bandwidth


class BandwidthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bandwidth
        fields = (
            'id',
            'url',
            'name',
            'address',
            'phone',
        )

    def validate_phone(self, value):
        phone_regex = r"^\+?1?-?\s*\(?([2-9][0-9]{2})\)?[-.\s]*([0-9]{3})[-.\s]*([0-9]{4})$"
        is_phone_valid = re.search(phone_regex, value)

        if not is_phone_valid:
            raise serializers.ValidationError("Phone number is not valid")

        return value
