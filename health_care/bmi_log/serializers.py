from rest_framework.serializers import ModelSerializer

from bmi_log.models import BMI


class BMISerializer(ModelSerializer):
    """
    Serializer for BMI model.
    """

    class Meta:
        fields = '__all__'
        model = BMI
