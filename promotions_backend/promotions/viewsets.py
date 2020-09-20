from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from promotions.serializers import PromotionLogSerializer
from promotions.models import PromotionLog
from datetime import datetime, timedelta

class PromotionLogViewSet(ModelViewSet):
    serializer_class = PromotionLogSerializer

    def get_queryset(self):
        return PromotionLog.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.data['status'] is None:
            response.data['status'] = -1
        return response

    def perform_create(self, serializer):
        # check if email used in last day
        if PromotionLog.objects.filter(
            email=serializer.initial_data['email'],
            created__gt=datetime.utcnow() - timedelta(days=1),
        ).exists():
            return
        response = super().perform_create(serializer)
        return response
