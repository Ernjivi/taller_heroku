from rest_framework.viewsets import ModelViewSet

from bmi_log.models import BMI
from bmi_log.serializers import BMISerializer

class BMIViewSet(ModelViewSet):
    """
    Creates, update, delete, list instances of BMI model.
    """

    queryset = BMI.objects.all()
    serializer_class = BMISerializer
