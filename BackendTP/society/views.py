from rest_framework import viewsets
from society.models import Plot, Video
from society.serializers import  PlotDetailSerializer, PlotSerializer, VideoSerializer, VideoDetailSerializer

class PlotViewset(viewsets.ModelViewSet):

    queryset = Plot.objects.all()
    serializer_class = PlotSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlotDetailSerializer
        return super().get_serializer_class()


class VideoViewset(viewsets.ModelViewSet):

    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VideoDetailSerializer
        return super().get_serializer_class()