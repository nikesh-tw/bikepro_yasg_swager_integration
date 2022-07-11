import base64
import json
from rest_framework import serializers
from .models import BikeDetail


def decode_bike_number(base64_bike_number):
    result, bike_num = False, None #1
    try:#2
        bike_num = base64.b64decode(base64_bike_number).decode('utf-8')
        result, bike_num = True, bike_num
    except Exception as e:#3
        result, bike_num = False, None
    return result, bike_num


class BikeDetailDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeDetail
        fields = ["name",'bike_number', 'employee_id']


class BikeDetailSerializer(serializers.Serializer):
    bike_number = serializers.CharField(required=True)

    def validate(self, data):
        encoded_bike_number = data.get('bike_number')
        result, bike_num = decode_bike_number(encoded_bike_number) #--use of decode_bike_number
        if result:
            bk_exist = BikeDetail.objects.filter(bike_number = bike_num).exists()
            if not bk_exist:
                return serializers.ValidationError("Bike Number does not exist in Database!!!")
        return data
