from rest_framework.serializers import ModelSerializer
from promotions.models import PromotionLog
import random
from datetime import datetime, timedelta

class PromotionLogSerializer(ModelSerializer):
    class Meta:
        model = PromotionLog
        fields = '__all__'

    def create(self, data):
        if PromotionLog.CODE_CHOICES[random.randint(0,4)][0] == data['code']:
            data['status'] = PromotionLog.STATUS_WON
        else:
            data['status'] = PromotionLog.STATUS_LOST
        return PromotionLog.objects.create(**data)
