# Create your views here.
from musics.models import Music
from musics.serializers import MusicSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
