from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from events.models import Event
from events.serializers import EventSerializer


# Create your views here.

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
